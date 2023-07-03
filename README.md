# to update, upgrade, and install python3 run the bellow commands
sudo apt update && sudo apt upgrade -y
sudo apt install python3
# to install the requirements run
pip3 install -r requirements.txt
# now get your api key and run to save your key in your session
export OPENAI_API_KEY="your_api_key"
# another option is to save this line in a file and to run the file like this
source your_file_name.sh
