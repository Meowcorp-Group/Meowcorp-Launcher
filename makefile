.PHONY: resources test

resources:
	echo "Updating "
	pyrcc5 -o resources/resources.py resources/resources.qrc

run:
	make resources
	python3 LMainWindow.py