LATEX = xelatex
PDFDIR = ../../../../pdf/controles/corriges/questionnements/
PYDIR  = ../../../../python/controles/questionnements/

export TEXINPUTS=.:../../../macros//:

ALLPDF = corriges-ds-info-S1-introduction.pdf\
		 corriges-ds-info-S1-affectation.pdf\
		 corriges-ds-info-S1-booleens.pdf\
		 corriges-ds-info-S1-codage.pdf\
		 corriges-ds-info-S1-tests.pdf\
		 corriges-ds-info-S1-boucles.pdf\
		 corriges-ds-info-S1-boucles-imbriquees.pdf\
		 corriges-ds-info-S1-boucles-polygones.pdf\
		 corriges-ds-info-S1-instructions.pdf\
		 corriges-ds-info-S1-ds.pdf\
		 corriges-ds-info-S1-recursivite.pdf\
		 corriges-ds-info-S1-sequences.pdf\
		 c-questionnements-info-S1.pdf

ALLPY = q-affectation.py\
		q-booleens.py\
		q-boucles-imbriquees.py\
		q-boucles-polygones.py\
		q-boucles.py\
		q-codage.py\
		q-conclusion.py\
		q-ds.py\
		q-instructions.py\
		q-introduction.py\
		q-recursivite.py\
		q-sequences.py\
		q-tests.py
	
#-------------------------------------------------------------------------------
all: $(ALLPDF) $(ALLPY)
	cp $(ALLPY) $(PYDIR)

#-------------------------------------------------------------------------------
%.pdf: %.tex
	$(LATEX) $<
	$(LATEX) $<
	cp $@ $(PDFDIR)

#-------------------------------------------------------------------------------
clean:
	rm -f $(ALLPDF)
	rm -f *.ald *.alx *.aux *.bbl *.blg *.bmt *.defd *.defx *.idx *.ilg *.ind
	rm -f *.log *.lol *.maf *.mtc* *.out *.tdd *.tdx *.thm *.toc 

