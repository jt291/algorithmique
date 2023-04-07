LATEX = xelatex
PDFDIR = ../../pdf/questionnements/
PYDIR = ../../../python/questionnements/

export TEXINPUTS=.:../macros//:

ALLPDF = q-info-S1.pdf

#-------------------------------------------------------------------------------
q-info-S1.pdf: q-info-S1.tex \
		q-info-S1-preambule.tex \
		q-info-S1-introduction.tex \
		q-info-S1-affectation.tex \
		q-info-S1-booleens.tex \
		q-info-S1-codage.tex \
		q-info-S1-tests.tex \
		q-info-S1-boucles.tex \
		q-info-S1-boucles-imbriquees.tex \
		q-info-S1-specification.tex \
		q-info-S1-recursivite.tex \
		q-info-S1-sequences.tex \
		q-info-S1-conclusion.tex 
	$(LATEX) q-info-S1.tex
	$(LATEX) q-info-S1.tex
	$(LATEX) q-info-S1.tex
	cp $(ALLPDF) $(PDFDIR)

#-------------------------------------------------------------------------------
clean:
	rm -f $(ALLPDF)
	rm -f *.ald *.alx *.aux *.bbl *.blg *.bmt *.defd *.defx *.idx *.ilg *.ind
	rm -f *.log *.lol *.maf *.mtc* *.out *.tdd *.tdx *.thm *.toc 

