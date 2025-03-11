from ._anvil_designer import MijnAnvilFormTemplate
from anvil import *
import anvil.server

class MijnAnvilForm(MijnAnvilFormTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    # Hoofdcontainer met styling
    layout = ColumnPanel(
      spacing="medium", 
      align="center", 
      background="#f0f8ff",  # Lichtblauw
      border="1px solid #d1e3ff",
      padding=20,
      role="card"
    )
    self.add_component(layout)

    # Stijlvolle titel
    title_label = Label(
      text="📊 Mijn Stijlvolle Anvil App", 
      bold=True, 
      font_size=28, 
      foreground="#0056b3",  # Donkerblauw
      align="center"
    )
    layout.add_component(title_label)

    # DataGrid met kolommen
    datagrid = DataGrid(
      border="1px solid #007bff",  
      background="#ffffff",
      spacing="small",
      role="card",
      width="90%"
    )
    datagrid.columns = [
        {"title": "ID", "data_key": "id"},
        {"title": "Naam", "data_key": "naam"},
        {"title": "Leeftijd", "data_key": "leeftijd"}
    ]

    # Voeg een RepeatingPanel toe aan de DataGrid
    repeating_panel = RepeatingPanel()
    repeating_panel.item_template = "RowTemplate"
    datagrid.add_component(repeating_panel)
    
    layout.add_component(datagrid)

    # FlowPanel voor de knoppen
    button_panel = FlowPanel(spacing="medium", align="center")
    layout.add_component(button_panel)

    # Stijlvolle knoppen
    add_button = Button(
      text="➕ Toevoegen",
      role="primary-button",
      background="#28a745",  # Groen
      foreground="#fff",
      border="none",
      font_size=16,
      bold=True
    )
    
    remove_button = Button(
      text="❌ Verwijderen",
      role="secondary-button",
      background="#dc3545",  # Rood
      foreground="#fff",
      border="none",
      font_size=16,
      bold=True
    )

    # Knoppen toevoegen
    button_panel.add_component(add_button)
    button_panel.add_component(remove_button)

    # Event handlers voor knoppen
    add_button.set_event_handler("click", self.on_add_click)
    remove_button.set_event_handler("click", self.on_remove_click)

  def on_add_click(self, **event_args):
    alert("✅ Je hebt een item toegevoegd!")

  def on_remove_click(self, **event_args):
    alert("⚠️ Een item is verwijderd.")
