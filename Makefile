all:
	#rm *.aux; true
	#pdflatex thesis
	# bibtex thesis
	#pdflatex thesis
	#pdflatex thesis
	xelatex thesis

archive:
	tar cvf thesis.tar.gz *.tex ??figs *.bib

clean:
	rm *.aux *.bbl *.blg *.log *.spl *~ \
	  thesis.pdf; true

