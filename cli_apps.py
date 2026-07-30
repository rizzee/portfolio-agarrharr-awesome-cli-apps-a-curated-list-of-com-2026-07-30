#!/usr/bin/env python3
"""
A simple CLI tool to browse curated command-line applications.
"""

import json
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table

# Main data file path
DATA_FILE = Path(__file__).parent / "data" / "cli_apps.json"


def load_apps() -> list[dict]:
    """Load apps from JSON data file."""
    try:
        return json.loads(DATA_FILE.read_text())
    except FileNotFoundError:
        click.echo(f"Error: Data file not found at {DATA_FILE}")
        raise click.Abort()


def print_table(apps: list[dict]):
    """Display apps in a rich table."""
    console = Console()
    table = Table(title="CLI Applications", show_header=True, header_style="bold magenta")
    
    table.add_column("Name")
    table.add_column("Category")
    table.add_column("Description")
    
    for app in apps:
        table.add_row(
            app["name"],
            app["category"],
            app["description"]
        )
    
    console.print(table)


@click.group()
def cli():
    """Main command group."""
    pass


@cli.command()
@click.option("--category", help="Filter by category")
def list_apps(category):
    """List all CLI applications."""
    apps = load_apps()
    
    if category:
        apps = [app for app in apps if app["category"].lower() == category.lower()]
    
    print_table(apps)


@cli.command()
@click.argument("query")
def search(query):
    """Search CLI applications by name or description."""
    apps = load_apps()
    matches = []
    
    query = query.lower()
    for app in apps:
        if query in app["name"].lower() or query in app["description"].lower():
            matches.append(app)
    
    print_table(matches)


if __name__ == "__main__":
    cli()
