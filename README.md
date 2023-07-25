# Update, upgrade, and install python3
sudo apt update && sudo apt upgrade -y
sudo apt install python3
# Install the requirements
pip3 install -r requirements.txt
# Export your API key
export OPENAI_API_KEY="your_api_key"
# Another option is to save this line in a file and to run the file like this
source your_file_name.sh
