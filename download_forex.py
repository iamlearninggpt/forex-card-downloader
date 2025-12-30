name: Download Forex Card Rates

on:
  schedule:
    # Runs daily at 9:00 AM IST (3:30 AM UTC)
    - cron: '30 3 * * *'
  
  # Allows manual trigger from Actions tab
  workflow_dispatch:

jobs:
  download:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install requests
    
    - name: Download Forex PDF
      run: |
        python download_forex.py
    
    - name: Commit and push if changed
      run: |
        git config --global user.name 'GitHub Action'
        git config --global user.email 'action@github.com'
        git add forex_rates/
        if ! git diff --quiet --staged; then
          git commit -m "Daily forex rates update $(date +'%Y-%m-%d')"
          git push
        fi
