"""
Ontology generation service.
API 1: analyze text content and generate entity and relationship type definitions
suitable for social media opinion simulation.
"""

import json
from typing import Dict, Any, List, Optional
from ..utils.llm_client import LLMClient


# System prompt for ontology generation
ONTOLOGY_SYSTEM_PROMPT = """You are a professional knowledge graph ontology designer. Your task is to analyze the given text content and simulation requirements, and design entity types and relationship types suitable for social media opinion simulation.

IMPORTANT: You must output valid JSON only. Do not output any other text.

## Core background

We are building a social media opinion simulation system. In this system:
- Each entity is an account or actor that can speak, interact, and spread information on social media
- Entities influence each other, repost, comment, and reply
- We need to simulate reactions and information diffusion paths in public opinion events

Therefore, entities must be real-world actors that can post and interact on social media.

Allowed examples:
- Individuals (public figures, parties involved, influencers, experts, ordinary people)
- Companies or enterprises (including official accounts)
- Organizations (universities, associations, NGOs, unions)
- Government departments or regulators
- Media organizations (newspapers, TV stations, self-media, websites)
- Social media platforms
- Representative groups (e.g., alumni groups, fan clubs, advocacy groups)

Not allowed:
- Abstract concepts (e.g., "public opinion", "sentiment", "trend")
- Topics or issues (e.g., "academic integrity", "education reform")
- Stances or attitudes (e.g., "supporters", "opponents")

## Output format

Please output JSON with the following structure:

```json
{
    "entity_types": [
        {
            "name": "EntityTypeName (English, PascalCase)",
            "description": "Short description (English, <= 100 characters)",
            "attributes": [
                {
                    "name": "attribute_name (English, snake_case)",
                    "type": "text",
                    "description": "Attribute description"
                }
            ],
            "examples": ["Example Entity 1", "Example Entity 2"]
        }
    ],
    "edge_types": [
        {
            "name": "RELATION_TYPE (English, UPPER_SNAKE_CASE)",
            "description": "Short description (English, <= 100 characters)",
            "source_targets": [
                {"source": "SourceEntityType", "target": "TargetEntityType"}
            ],
            "attributes": []
        }
    ],
    "analysis_summary": "Brief analysis of the text content (English)"
}
```

## Design guidelines (very important)

### 1. Entity type design - must follow strictly

Quantity requirement: output exactly 10 entity types.

Hierarchy requirement (must include both specific types and fallback types):

Your 10 entity types must include:

A. Fallback types (must include, and place as the last two in the list):
   - `Person`: a fallback for any individual who does not fit other specific person types.
   - `Organization`: a fallback for any organization that does not fit other specific organization types.

B. Specific types (8 types, designed based on the text):
   - Target key roles that appear frequently or are central to the text
   - Example: for academic topics, you might include `Student`, `Professor`, `University`
   - Example: for business topics, you might include `Company`, `CEO`, `Employee`

Why fallback types are needed:
- The text may include various people like "primary school teacher", "passerby", "some netizen"
- If there is no exact match, they should fall under `Person`
- Similarly, small organizations or temporary groups should fall under `Organization`

Specific type principles:
- Identify high-frequency or key roles from the text
- Each specific type should have clear boundaries and avoid overlap
- The description must clearly differentiate it from the fallback type

### 2. Relationship type design

- Count: 6-10
- Relationships should reflect real social media interactions
- Ensure source_targets covers your defined entity types

### 3. Attribute design

- 1-3 key attributes per entity type
- Attribute names cannot use reserved names such as `name`, `uuid`, `group_id`, `created_at`, `summary`
- Recommended names: `full_name`, `title`, `role`, `position`, `location`, `description`

## Entity type references

Individuals (specific examples):
- Student
- Professor
- Journalist
- Celebrity
- Executive
- Official
- Lawyer
- Doctor

Individuals (fallback):
- Person: any individual not covered by specific types

Organizations (specific examples):
- University
- Company
- GovernmentAgency
- MediaOutlet
- Hospital
- School
- NGO

Organizations (fallback):
- Organization: any organization not covered by specific types

## Relationship type references

- WORKS_FOR
- STUDIES_AT
- AFFILIATED_WITH
- REPRESENTS
- REGULATES
- REPORTS_ON
- COMMENTS_ON
- RESPONDS_TO
- SUPPORTS
- OPPOSES
- COLLABORATES_WITH
- COMPETES_WITH
"""


class OntologyGenerator:
    """
    Ontology generator.
    Analyzes text content and produces entity and relationship definitions.
    """

    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm_client = llm_client or LLMClient()

    def generate(
        self,
        document_texts: List[str],
        simulation_requirement: str,
        additional_context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate ontology definitions.

        Args:
            document_texts: List of document text
            simulation_requirement: Simulation requirement description
            additional_context: Extra context

        Returns:
            Ontology definition (entity_types, edge_types, etc.)
        """
        # Build user message
        user_message = self._build_user_message(
            document_texts,
            simulation_requirement,
            additional_context
        )

        messages = [
            {"role": "system", "content": ONTOLOGY_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]

        # Call LLM
        result = self.llm_client.chat_json(
            messages=messages,
            temperature=0.3,
            max_tokens=4096
        )

        # Validate and post-process
        result = self._validate_and_process(result)

        return result

    # Max text length sent to LLM (50k chars)
    MAX_TEXT_LENGTH_FOR_LLM = 50000

    def _build_user_message(
        self,
        document_texts: List[str],
        simulation_requirement: str,
        additional_context: Optional[str]
    ) -> str:
        """Build user prompt."""

        # Combine text
        combined_text = "\n\n---\n\n".join(document_texts)
        original_length = len(combined_text)

        # If text exceeds 50k chars, truncate for the LLM only
        if len(combined_text) > self.MAX_TEXT_LENGTH_FOR_LLM:
            combined_text = combined_text[:self.MAX_TEXT_LENGTH_FOR_LLM]
            combined_text += (
                f"\n\n...(original length {original_length} chars, "
                f"truncated to {self.MAX_TEXT_LENGTH_FOR_LLM} chars for ontology analysis)..."
            )

        message = f"""## Simulation Requirement

{simulation_requirement}

## Document Content

{combined_text}
"""

        if additional_context:
            message += f"""
## Additional Notes

{additional_context}
"""

        message += """
Please design entity types and relationship types suitable for social media opinion simulation based on the content above.

Rules you must follow:
1. Output exactly 10 entity types
2. The last two must be fallback types: Person (individual fallback) and Organization (organization fallback)
3. The first 8 are specific types designed from the text
4. All entity types must be real-world actors that can post on social media, not abstract concepts
5. Attribute names cannot use reserved names like name, uuid, group_id; use full_name, org_name, etc.
"""

        return message

    def _validate_and_process(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and post-process the result."""

        # Ensure required fields exist
        if "entity_types" not in result:
            result["entity_types"] = []
        if "edge_types" not in result:
            result["edge_types"] = []
        if "analysis_summary" not in result:
            result["analysis_summary"] = ""

        # Validate entity types
        for entity in result["entity_types"]:
            if "attributes" not in entity:
                entity["attributes"] = []
            if "examples" not in entity:
                entity["examples"] = []
            # Ensure description <= 100 chars
            if len(entity.get("description", "")) > 100:
                entity["description"] = entity["description"][:97] + "..."

        # Validate edge types
        for edge in result["edge_types"]:
            if "source_targets" not in edge:
                edge["source_targets"] = []
            if "attributes" not in edge:
                edge["attributes"] = []
            if len(edge.get("description", "")) > 100:
                edge["description"] = edge["description"][:97] + "..."

        # Zep API limits: up to 10 custom entity types and 10 custom edge types
        MAX_ENTITY_TYPES = 10
        MAX_EDGE_TYPES = 10

        # Fallback type definitions
        person_fallback = {
            "name": "Person",
            "description": "Any individual person not fitting other specific person types.",
            "attributes": [
                {"name": "full_name", "type": "text", "description": "Full name of the person"},
                {"name": "role", "type": "text", "description": "Role or occupation"}
            ],
            "examples": ["ordinary citizen", "anonymous netizen"]
        }

        organization_fallback = {
            "name": "Organization",
            "description": "Any organization not fitting other specific organization types.",
            "attributes": [
                {"name": "org_name", "type": "text", "description": "Name of the organization"},
                {"name": "org_type", "type": "text", "description": "Type of organization"}
            ],
            "examples": ["small business", "community group"]
        }

        # Check for existing fallback types
        entity_names = {e["name"] for e in result["entity_types"]}
        has_person = "Person" in entity_names
        has_organization = "Organization" in entity_names

        # Fallbacks to add
        fallbacks_to_add = []
        if not has_person:
            fallbacks_to_add.append(person_fallback)
        if not has_organization:
            fallbacks_to_add.append(organization_fallback)

        if fallbacks_to_add:
            current_count = len(result["entity_types"])
            needed_slots = len(fallbacks_to_add)

            # If adding exceeds 10, remove from the end
            if current_count + needed_slots > MAX_ENTITY_TYPES:
                to_remove = current_count + needed_slots - MAX_ENTITY_TYPES
                result["entity_types"] = result["entity_types"][:-to_remove]

            # Add fallback types
            result["entity_types"].extend(fallbacks_to_add)

        # Final guard against limits
        if len(result["entity_types"]) > MAX_ENTITY_TYPES:
            result["entity_types"] = result["entity_types"][:MAX_ENTITY_TYPES]

        if len(result["edge_types"]) > MAX_EDGE_TYPES:
            result["edge_types"] = result["edge_types"][:MAX_EDGE_TYPES]

        return result

    def generate_python_code(self, ontology: Dict[str, Any]) -> str:
        """
        Convert ontology definition into Python code (similar to ontology.py).

        Args:
            ontology: Ontology definition

        Returns:
            Python code string
        """
        code_lines = [
            '"""',
            'Custom entity type definitions',
            'Generated by HamroFish for social media opinion simulation',
            '"""',
            '',
            'from pydantic import Field',
            'from zep_cloud.external_clients.ontology import EntityModel, EntityText, EdgeModel',
            '',
            '',
            '# ============== Entity Type Definitions ==============',
            '',
        ]

        # Generate entity types
        for entity in ontology.get("entity_types", []):
            name = entity["name"]
            desc = entity.get("description", f"A {name} entity.")

            code_lines.append(f'class {name}(EntityModel):')
            code_lines.append(f'    """{desc}"""')

            attrs = entity.get("attributes", [])
            if attrs:
                for attr in attrs:
                    attr_name = attr["name"]
                    attr_desc = attr.get("description", attr_name)
                    code_lines.append('    ' + f"{attr_name}: EntityText = Field(")
                    code_lines.append('        ' + f"description=\"{attr_desc}\",")
                    code_lines.append('        default=None')
                    code_lines.append('    )')
            else:
                code_lines.append('    pass')

            code_lines.append('')
            code_lines.append('')

        code_lines.append('# ============== Relationship Type Definitions ==============')
        code_lines.append('')

        # Generate relationship types
        for edge in ontology.get("edge_types", []):
            name = edge["name"]
            # Convert to PascalCase class name
            class_name = ''.join(word.capitalize() for word in name.split('_'))
            desc = edge.get("description", f"A {name} relationship.")

            code_lines.append(f'class {class_name}(EdgeModel):')
            code_lines.append(f'    """{desc}"""')

            attrs = edge.get("attributes", [])
            if attrs:
                for attr in attrs:
                    attr_name = attr["name"]
                    attr_desc = attr.get("description", attr_name)
                    code_lines.append('    ' + f"{attr_name}: EntityText = Field(")
                    code_lines.append('        ' + f"description=\"{attr_desc}\",")
                    code_lines.append('        default=None')
                    code_lines.append('    )')
            else:
                code_lines.append('    pass')

            code_lines.append('')
            code_lines.append('')

        # Generate type mappings
        code_lines.append('# ============== Type Config ==============')
        code_lines.append('')
        code_lines.append('ENTITY_TYPES = {')
        for entity in ontology.get("entity_types", []):
            name = entity["name"]
            code_lines.append(f'    "{name}": {name},')
        code_lines.append('}')
        code_lines.append('')
        code_lines.append('EDGE_TYPES = {')
        for edge in ontology.get("edge_types", []):
            name = edge["name"]
            class_name = ''.join(word.capitalize() for word in name.split('_'))
            code_lines.append(f'    "{name}": {class_name},')
        code_lines.append('}')
        code_lines.append('')

        # Generate source_targets mappings
        code_lines.append('EDGE_SOURCE_TARGETS = {')
        for edge in ontology.get("edge_types", []):
            name = edge["name"]
            source_targets = edge.get("source_targets", [])
            if source_targets:
                st_list = ', '.join([
                    f'{{"source": "{st.get("source", "Entity")}", "target": "{st.get("target", "Entity")}"}}'
                    for st in source_targets
                ])
                code_lines.append(f'    "{name}": [{st_list}],')
        code_lines.append('}')

        return '\n'.join(code_lines)
