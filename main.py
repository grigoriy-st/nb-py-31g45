from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()
table = Table(title="Books")
table.add_column("Title")
table.add_column("Author")
table.add_row("Clean Code", "R Martin")

console.print(table)
