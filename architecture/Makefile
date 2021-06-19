PLANTUML_JAR_URL = https://sourceforge.net/projects/plantuml/files/plantuml.jar/download

# If the JAR file isn't already present, download it
download:
	curl -sSfL $(PLANTUML_JAR_URL) -o plantuml.jar

# Each PNG output depends on its corresponding .plantuml file
generate: 
	java -jar plantuml.jar -tpng "puml/*.plantuml" -o "../img/"