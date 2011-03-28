all:
	rm *.aux; true
	xelatex thesis
	bibtex thesis
	xelatex thesis
	xelatex thesis

archive:
	tar cvf thesis.tar.gz *.tex ??figs *.bib aux

clean:
	rm *.aux *.bbl *.blg *.log *.spl *~ \
	  thesis.pdf; true

