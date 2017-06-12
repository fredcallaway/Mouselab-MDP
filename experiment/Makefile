# Compile coffeescript into javascript
all: 
	coffee -o static/js -cb src/*
	bin/make_trials.py

# Continuously recompiles as changes are made.
watch:
	coffee -o static/js -cbw src/*

deploy:
	rsync -av --delete-after --copy-links . cocosci@cocosci-fred.dreamhosters.com:/home/cocosci/cocosci.dreamhosters.com/webexpt/mouselab-demo