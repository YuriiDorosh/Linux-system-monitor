# Variables
ENV_NAME = env
ENV_ACTIVATE = $(ENV_NAME)/bin/activate
PYTHON = $(ENV_NAME)/bin/python3
PIP = $(ENV_NAME)/bin/pip3

# Targets

all: setup run

setup:
	# Ensure bash script is executable
	chmod +x build_and_run.sh
	# Execute the setup script
	./build_and_run.sh

env: $(ENV_ACTIVATE)
$(ENV_ACTIVATE): requirements.txt
	test -d $(ENV_NAME) || python3 -m venv $(ENV_NAME)
	$(PIP) install -r requirements.txt
	touch $(ENV_ACTIVATE)

install-deps:
	sudo apt update
	sudo apt install python3-tk ffmpeg scrot git python3 pip3

clone:
	git clone https://github.com/YuriiDorosh/Linux-system-monitor.git

run-gui:
	$(PYTHON) src/main.py -g

run-console:
	$(PYTHON) src/main.py -c

run-settings:
	$(PYTHON) src/main.py --settings

run:
	@echo "How would you like to run the project?"
	@echo "1. Greeting window"
	@echo "2. GUI Version"
	@echo "3. Console version"
	@echo "4. Settings"
	@read -p "Choose a number [1-4]: " choice; \
	case $$choice in \
		1) $(MAKE) run-gui ;; \
		2) $(MAKE) run-gui ;; \
		3) $(MAKE) run-console ;; \
		4) $(MAKE) run-settings ;; \
		*) echo "Invalid choice. Exiting." ;; \
	esac

clean:
	rm -rf $(ENV_NAME)

.PHONY: all setup env install-deps clone run-gui run-console run-settings run clean
