LATEX = xelatex
PDFDIR = ../../pdf/cours/

export TEXINPUTS=.:../macros//:

ALLPDF = info-S1.pdf

#-------------------------------------------------------------------------------
info-S1.pdf: info-S1.tex \
	info-S1-introduction.tex \
	info-S1-instructions.tex \
	info-S1-fonctions.tex \
	info-S1-listes.tex \
	info-S1-exercices.tex \
	info-S1-classiques.tex \
	info-S1.bib
	$(LATEX) info-S1.tex
	bibtex info-S1
	makeindex info-S1
	makeindex info-S1.alx -o info-S1.ald
	makeindex info-S1.defx -o info-S1.defd
	makeindex info-S1.tdx -o info-S1.tdd
	$(LATEX) info-S1.tex
	$(LATEX) info-S1.tex
	cp info-S1.pdf $(PDFDIR)

#-------------------------------------------------------------------------------
clean:
	rm -f $(ALLPDF)
	rm -f *.ald *.alx *.aux *.bbl *.blg *.bmt *.defd *.defx *.idx *.ilg *.ind
	rm -f *.log *.lol *.maf *.mtc* *.out *.tdd *.tdx *.thm *.toc 
