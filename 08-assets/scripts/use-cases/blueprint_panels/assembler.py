"""
Blueprint Assembler
Combines modular panels into complete blueprints with configurable layouts.
"""

import csv
from typing import Dict, List
from .base import XMLCellBuilder, Position, StandardLayout, build_diagram


def load_csv_file(filename: str) -> List[Dict]:
    """Load CSV file and return list of dictionaries."""
    with open(filename, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


class BlueprintAssembler:
    """Assembles panels into complete blueprints."""
    
    def __init__(self):
        self.builder = XMLCellBuilder()
        self.all_cells = []
        self.data_cache = {}
    
    def load_all_data(self):
        """Load all data files once."""
        if self.data_cache:
            return  # Already loaded
        
        files = [
            'use-case-summary.csv',
            'use-case-metrics.csv',
            'use-case-governance.csv',
            'use-case-risks.csv',
            'use-case-success-metrics.csv',
            'use-case-costing.csv',
            'use-case-resources.csv',
            'use-case-systems-volume.csv',
            'use-case-phases.csv',
            'solution-abb-catalog.csv',
            'solution-interfaces-catalog.csv',
            'ai-architecture-building-blocks.csv',
        ]
        
        for filename in files:
            key = filename.replace('.csv', '').replace('-', '_')
            self.data_cache[key] = load_csv_file(filename)
    
    def get_use_case_data(self, use_case_id: int) -> Dict:
        """
        Get all data for a specific use case.
        
        Args:
            use_case_id: Use case ID
            
        Returns:
            Dictionary with all use case data
        """
        self.load_all_data()
        
        # Filter data for this use case
        data = {}
        
        # Single-row data
        data['summary'] = next(r for r in self.data_cache['use_case_summary']
                              if int(r['use_case_id']) == use_case_id)
        data['metrics'] = next(r for r in self.data_cache['use_case_metrics']
                              if int(r['use_case_id']) == use_case_id)
        data['governance'] = next(r for r in self.data_cache['use_case_governance']
                                 if int(r['use_case_id']) == use_case_id)
        data['risks'] = next(r for r in self.data_cache['use_case_risks']
                            if int(r['use_case_id']) == use_case_id)
        data['success'] = next(r for r in self.data_cache['use_case_success_metrics']
                              if int(r['use_case_id']) == use_case_id)
        data['costing'] = next(r for r in self.data_cache['use_case_costing']
                              if int(r['use_case_id']) == use_case_id)
        data['resources'] = next(r for r in self.data_cache['use_case_resources']
                                if int(r['use_case_id']) == use_case_id)
        data['systems'] = next(r for r in self.data_cache['use_case_systems_volume']
                              if int(r['use_case_id']) == use_case_id)
        
        # Multi-row data
        data['phases'] = [r for r in self.data_cache['use_case_phases']
                         if int(r['use_case_id']) == use_case_id]
        data['abbs'] = [r for r in self.data_cache['solution_abb_catalog']
                       if int(r['use_case_id']) == use_case_id]
        data['interfaces'] = [r for r in self.data_cache['solution_interfaces_catalog']
                             if int(r['use_case_id']) == use_case_id]
        
        # Reference data
        data['all_abbs'] = self.data_cache['ai_architecture_building_blocks']
        
        return data
    
    def assemble_full_blueprint(self, use_case_id: int, layout: str = "standard") -> str:
        """
        Assemble a complete blueprint using specified layout.
        
        Args:
            use_case_id: Use case ID
            layout: Layout template name (default: "standard")
            
        Returns:
            Complete draw.io XML string
        """
        # Get data
        uc_data = self.get_use_case_data(use_case_id)
        
        # Import panel modules
        from . import (header_panel, summary_panel, metrics_panel, governance_panel,
                      change_impact_panel, decision_panel, components_panel,
                      interfaces_panel, tech_stack_panel, risk_panel,
                      success_metrics_panel, phases_panel, resources_panel,
                      costing_panel, info_boxes_panel, connections_panel,
                      footer_panel)
        
        cells = []
        
        # Apply layout template
        if layout == "standard":
            # Full blueprint with all panels
            
            # 1. Header
            cells.extend(header_panel.create(self.builder, {
                'use_case_id': use_case_id,
                'use_case_name': uc_data['summary']['use_case_name'],
                'improved_description': uc_data['summary'].get('improved_description', '')
            }))
            
            # 2. Summary Panel (top left)
            cells.extend(summary_panel.create(
                self.builder,
                uc_data['summary'],
                Position(30, 110, 580, 280)
            ))
            
            # 3. Metrics Panel (middle left)
            cells.extend(metrics_panel.create(
                self.builder,
                uc_data['metrics'],
                Position(30, 410, 285, 140)
            ))
            
            # 4. Governance Panel (middle left, second column)
            cells.extend(governance_panel.create(
                self.builder,
                uc_data['governance'],
                Position(325, 410, 285, 140)
            ))
            
            # 5. Change Impact Panel (bottom left)
            cells.extend(change_impact_panel.create(
                self.builder,
                {**uc_data['risks'], 'complexity': uc_data['costing']['complexity']},
                Position(30, 570, 285, 150)
            ))
            
            # 6. Decision Panel (bottom left, second column)
            cells.extend(decision_panel.create(
                self.builder,
                uc_data['risks'],
                Position(325, 570, 285, 150)
            ))
            
            # 7. Components Panel (center)
            comp_result = components_panel.create(
                self.builder,
                {'abbs': uc_data['abbs'], 'interfaces': uc_data['interfaces']},
                Position(640, 110, 840, 640)
            )
            cells.extend(comp_result['cells'])
            abb_positions = comp_result['abb_positions']
            
            # 8. Connections (on top of components)
            cells.extend(connections_panel.create(
                self.builder,
                {'interfaces': uc_data['interfaces']},
                abb_positions
            ))
            
            # 9. Info Boxes + Legend (bottom of components area)
            cells.extend(info_boxes_panel.create(
                self.builder,
                uc_data['systems'],
                Position(0, 680, 0, 0)  # Y position only
            ))
            
            # 10. Interface Catalog (bottom left large)
            cells.extend(interfaces_panel.create(
                self.builder,
                {'interfaces': uc_data['interfaces']},
                Position(30, 740, 580, 310)
            ))
            
            # 11. Technical Stack (top right)
            cells.extend(tech_stack_panel.create(
                self.builder,
                {'abbs': uc_data['abbs'], 'all_abbs': uc_data['all_abbs']},
                Position(1510, 110, 380, 190)
            ))
            
            # 12. Risk Assessment (middle right)
            cells.extend(risk_panel.create(
                self.builder,
                uc_data['risks'],
                Position(1510, 320, 380, 210)
            ))
            
            # 13. Success Metrics (middle-bottom right)
            cells.extend(success_metrics_panel.create(
                self.builder,
                uc_data['success'],
                Position(1510, 550, 380, 200)
            ))
            
            # 14. Implementation Roadmap (bottom center)
            cells.extend(phases_panel.create(
                self.builder,
                {'phases': uc_data['phases']},
                Position(640, 770, 420, 280)
            ))
            
            # 15. Resources (bottom center-right)
            cells.extend(resources_panel.create(
                self.builder,
                uc_data['resources'],
                Position(1080, 770, 410, 280)
            ))
            
            # 16. Costing Footer (bottom right)
            cells.extend(costing_panel.create(
                self.builder,
                {**uc_data['costing'], 'stakeholders': uc_data['summary'].get('enterprise_architect', '')},
                Position(1510, 770, 380, 280)
            ))
            
            # 17. Document Footer
            cells.append(footer_panel.create(
                self.builder,
                uc_data['summary']
            ))
        
        elif layout == "technical":
            # Technical-only blueprint (components, interfaces, tech stack)
            cells.extend(header_panel.create(self.builder, {
                'use_case_id': use_case_id,
                'use_case_name': uc_data['summary']['use_case_name'],
                'improved_description': uc_data['summary'].get('improved_description', '')
            }))
            
            comp_result = components_panel.create(
                self.builder,
                {'abbs': uc_data['abbs'], 'interfaces': uc_data['interfaces']},
                Position(30, 110, 840, 640)
            )
            cells.extend(comp_result['cells'])
            
            cells.extend(connections_panel.create(
                self.builder,
                {'interfaces': uc_data['interfaces']},
                comp_result['abb_positions']
            ))
            
            cells.extend(tech_stack_panel.create(
                self.builder,
                {'abbs': uc_data['abbs'], 'all_abbs': uc_data['all_abbs']},
                Position(900, 110, 380, 600)
            ))
            
            cells.extend(interfaces_panel.create(
                self.builder,
                {'interfaces': uc_data['interfaces']},
                Position(900, 730, 980, 320)
            ))
            
            cells.append(footer_panel.create(self.builder, uc_data['summary']))
        
        elif layout == "business":
            # Business-only blueprint (summary, metrics, risks, costing, resources)
            cells.extend(header_panel.create(self.builder, {
                'use_case_id': use_case_id,
                'use_case_name': uc_data['summary']['use_case_name'],
                'improved_description': uc_data['summary'].get('improved_description', '')
            }))
            
            cells.extend(summary_panel.create(
                self.builder,
                uc_data['summary'],
                Position(30, 110, 600, 300)
            ))
            
            cells.extend(metrics_panel.create(
                self.builder,
                uc_data['metrics'],
                Position(650, 110, 600, 150)
            ))
            
            cells.extend(governance_panel.create(
                self.builder,
                uc_data['governance'],
                Position(1270, 110, 600, 150)
            ))
            
            cells.extend(risk_panel.create(
                self.builder,
                uc_data['risks'],
                Position(30, 430, 600, 300)
            ))
            
            cells.extend(success_metrics_panel.create(
                self.builder,
                uc_data['success'],
                Position(650, 430, 600, 300)
            ))
            
            cells.extend(costing_panel.create(
                self.builder,
                {**uc_data['costing'], 'stakeholders': uc_data['summary'].get('enterprise_architect', '')},
                Position(1270, 430, 600, 300)
            ))
            
            cells.extend(phases_panel.create(
                self.builder,
                {'phases': uc_data['phases']},
                Position(30, 750, 900, 280)
            ))
            
            cells.extend(resources_panel.create(
                self.builder,
                uc_data['resources'],
                Position(950, 750, 920, 280)
            ))
            
            cells.append(footer_panel.create(self.builder, uc_data['summary']))
        
        # Build complete XML
        uc_name = uc_data['summary']['use_case_name']
        return build_diagram(cells, use_case_id, uc_name)
    
    def save_blueprint(self, use_case_id: int, layout: str = "standard", output_dir: str = ".."):
        """
        Generate and save a blueprint.
        
        Args:
            use_case_id: Use case ID
            layout: Layout template name
            output_dir: Output directory
            
        Returns:
            Filename of saved blueprint
        """
        xml = self.assemble_full_blueprint(use_case_id, layout)
        
        # Get use case name for filename
        uc_data = self.get_use_case_data(use_case_id)
        uc_name = uc_data['summary']['use_case_name']
        uc_name_clean = uc_name.replace(' ', '-').replace('/', '-').replace(',', '')[:40]
        
        filename = f"{output_dir}/UC-{use_case_id:03d}-{uc_name_clean}-Blueprint-{layout.title()}-v1.0.0.drawio"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml)
        
        return filename


def generate_blueprint(use_case_id: int, layout: str = "standard", output_dir: str = "..") -> str:
    """
    Convenience function to generate a blueprint.
    
    Args:
        use_case_id: Use case ID (1-24)
        layout: Layout template ("standard", "technical", "business")
        output_dir: Output directory
        
    Returns:
        Filename of generated blueprint
    """
    assembler = BlueprintAssembler()
    return assembler.save_blueprint(use_case_id, layout, output_dir)

