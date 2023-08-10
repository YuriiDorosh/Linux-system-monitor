# Setting Up and Running the Linux System Monitor

## Installation

### Prerequisites

Before using the Linux System Monitor, ensure you have the following dependencies installed:

- `ffmpeg`
- `scrot`
- `git`
- `python3`
- `python3-tk`
- `pip3`

 Update the package list:

```bash
sudo apt update
```

 Install Tkinter:
 
```bash
sudo apt install python3-tk
```

 Install ffmpeg:

```bash
sudo apt install ffmpeg
```

 Install scrot:

```bash
sudo apt-get install scrot
```
   
 Clone this repository:

```bash
git clone https://github.com/YuriiDorosh/Linux-system-monitor.git
```

 Set up a virtual environment:

```bash
python3 -m venv env
```

 Activate the virtual environment:
    
```bash
source env/bin/activate
```
 Install required Python packages:

```bash
pip3 install -r requirements.txt
```


## Usage 

Navigate to the src/ directory:

```bash
cd src/
```

### Greeting window


```bash
python3 main.py 
```

### GUI Version


Run the following command to launch the GUI version:

```bash
python3 main.py -g
```

Alternatively, you can use the long version:
    
```bash
python3 main.py --gui
```    

### Console version



Run the following command to launch the console version:


```bash
python3 main.py -c
```

Alternatively, you can use the long version:
    
```bash
python3 main.py --console
```    

### Settings

Run the following command to launch the settings of the app:

```bash
python3 main.py --s
```  

Alternatively, you can use the long version:
    
```bash
python3 main.py --settings
```    
