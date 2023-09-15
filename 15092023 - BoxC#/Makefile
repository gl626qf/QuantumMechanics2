# Makefile

# Set the name of your C# source file (without the extension)
CS_SRC = Program

# Set the name of the Gnuplot script file (without the extension)
GPI_SCRIPT = contour_plotm

# Set the output folder for the generated files
OUTPUT_DIR = Output

# Define the default target (what happens when you just run 'make' without any target)
all: build_cs 

# Target for building the C# executable
build_cs:
	@echo "Building C# executable..."
	@mkdir -p $(OUTPUT_DIR)
	@mcs -out:$(OUTPUT_DIR)/$(CS_SRC).exe SourceCode/$(CS_SRC).cs

# Target for building the Gnuplot script
build_gpi:
	@echo "Building Gnuplot script..."
	@cp $(GPI_SCRIPT).gpi $(OUTPUT_DIR)
	@cd $(OUTPUT_DIR) && gnuplot $(GPI_SCRIPT).gpi

# Target for cleaning (removing) the generated files
clean:
	@echo "Cleaning..."
	@rm -rf $(OUTPUT_DIR)

# Target for running the C# executable
run:
	@mono $(OUTPUT_DIR)/$(CS_SRC).exe
