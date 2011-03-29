all:
	rm *.aux; true
	xelatex thesis
	bibtex 01intro
	bibtex 02code
	#bibtex 03ssc 
	#bibtex 05moon
	#bibtex 06fluffy
	xelatex thesis
	xelatex thesis

archive:
	tar cvf thesis.tar.gz *.tex ??figs *.bib aux

clean:
	rm *.aux *.bbl *.blg *.log *.spl *~ \
	  thesis.pdf; true

