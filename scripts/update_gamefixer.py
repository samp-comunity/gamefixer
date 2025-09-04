name: Update Stats

on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout gamefixer repo
        uses: actions/checkout@v3

      - name: Checkout plujin-manager repo
        uses: actions/checkout@v3
        with:
          repository: samp-comunity/plujin-manager
          path: plujin-manager
          token: ${{ secrets.PLUGIN_MANAGER_TOKEN }}

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests

      - name: Run update script
        run: python scripts/update_gamefixer.py

      - name: Commit and push changes
        run: |
          cd plujin-manager
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add assets/scripts.json
          git commit -m "chore: auto update GameFixer stats" || echo "No changes to commit"
          git push
