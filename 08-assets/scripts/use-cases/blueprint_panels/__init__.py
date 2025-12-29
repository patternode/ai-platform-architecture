"""
Modular Blueprint Panel System for BNZ AI Use Cases

This package provides reusable panel modules that can be assembled
into different blueprint formats.

Usage:
    from blueprint_panels import base, header_panel, summary_panel
    from blueprint_panels.assembler import BlueprintAssembler
    
    assembler = BlueprintAssembler()
    assembler.add_panel(header_panel.create(...))
    assembler.add_panel(summary_panel.create(...))
    xml = assembler.build()
"""

__version__ = "1.0.0"
__all__ = [
    "base",
    "header_panel",
    "summary_panel",
    "metrics_panel",
    "governance_panel",
    "components_panel",
    "interfaces_panel",
    "tech_stack_panel",
    "risk_panel",
    "success_metrics_panel",
    "phases_panel",
    "resources_panel",
    "costing_panel",
    "info_boxes_panel",
    "assembler",
]

