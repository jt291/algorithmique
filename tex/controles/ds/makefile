LATEX = xelatex
PDFDIR = ../../../pdf/controles/ds/

export TEXINPUTS=.:../../macros//:

ALLPDF = ds-algo-01.pdf\
		 ds-algo-02.pdf\
		 ds-algo-03.pdf\
		 ds-algo-04.pdf\
		 ds-algo-05.pdf\
		 ds-algo-06.pdf\
		 ds-algo-07.pdf\
		 ds-algo-08.pdf\
		 ds-algo-09.pdf\
		 ds-algo-10.pdf\
		 ds-instruc-01.pdf\
		 ds-instruc-02.pdf\
		 ds-instruc-03.pdf\
		 ds-instruc-04.pdf\
		 ds-instruc-05.pdf\
		 ds-instruc-06.pdf\
		 ds-instruc-07.pdf

#-------------------------------------------------------------------------------
all: $(ALLPDF)
	
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
