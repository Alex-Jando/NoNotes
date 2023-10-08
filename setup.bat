echo "Installing requirements..."
python -m pip install -r requirements.txt
python -c "import nltk;nltk.download('punkt')"
echo "Setup Complete!"
pause