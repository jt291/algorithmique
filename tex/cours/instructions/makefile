LATEX = pdflatex
PDFDIR = ../../../pdf/cours

export TEXINPUTS=.:../../macros//:

ALLPDF = instructionsSlide.pdf instructionsPaper.pdf

#------------------------------------------------------------------------------------------
all: $(ALLPDF)

#------------------------------------------------------------------------------------------
%.pdf: %.tex
	$(LATEX) $<
	$(LATEX) $<
	cp $@ $(PDFDIR)

#------------------------------------------------------------------------------------------
clean:
	rm -f *.aux *.log *.mtc* *.nav *.out *.snm *.thm *.toc
	rm -f $(ALLPDF)

