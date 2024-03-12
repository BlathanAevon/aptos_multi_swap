if test -d ./venv; then
    echo "Venv is already created, running script..."
else 
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
    
source venv/bin/activate

echo "Installing requirements..."
pip install -q -r requirements.txt
echo "Requirements installed!"
python main.py