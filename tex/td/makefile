LATEX = xelatex
PDFDIR = ../../pdf/td/

export TEXINPUTS=.:../macros//:

td-info-S1.pdf: td-info-S1.tex \
	td-info-S1-introduction.tex \
	td-info-S1-instructions.tex \
	td-info-S1-fonctions.tex \
	td-info-S1-listes.tex \
	td-info-S1-annexes.tex 
	$(LATEX) td-info-S1.tex
	$(LATEX) td-info-S1.tex
	$(LATEX) td-info-S1.tex
	cp td-info-S1.pdf $(PDFDIR)

clean:
	rm -f td-info-S1.pdf
	rm -f *.alx *.aux *.defx *.ha* *.hi* *.ht* *.idx *.log 
	rm -f *.maf *.mt* *.out *.tdx *.thm *.toc

