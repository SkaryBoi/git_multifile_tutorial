# imports the file adjacent to this (this being the main file) as if it were any other module
# it's good practice(?) to have .py files that are not the main file in a separate folder
# since this file is in a separate folder, you have to reference <folder>.<file> like a directory
# if you don't import "as", you will have to reference <folder>.<file> each time, not just <file> like most external modules
import modules.module as module

# declares variable for use later
mainvar = "this variable is from main"

# uses variable declared in module
print(module.modulevar)
print(mainvar)
