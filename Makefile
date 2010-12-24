all:
	rm *.aux; true
	pdflatex thesis
	# bibtex thesis
	pdflatex thesis
	pdflatex thesis

clean:
	rm *.aux *.bbl *.blg *.log *.spl *~ \
	  thesis.pdf; true

