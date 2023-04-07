
#-------------------------------------------------------------------------------
all: plan\
	 diapos\
	 notes\
	 supports\
	 tdnotes\
	 questions\
	 ds\
	 mvrpaper

#-------------------------------------------------------------------------------
diapos: introductionSlide\
		instructionsSlide\
		fonctions-1Slide\
		fonctions-2Slide\
		listesSlide

introductionSlide:
	(cd cours/introduction/; make introductionSlide.pdf)
	
instructionsSlide:
	(cd cours/instructions/; make instructionsSlide.pdf)
	
fonctions-1Slide:
	(cd cours/fonctions/; make fonctions-1Slide.pdf)

fonctions-2Slide:
	(cd cours/fonctions/; make fonctions-2Slide.pdf)

listesSlide: 
	(cd cours/listes/; make listesSlide.pdf)

#-------------------------------------------------------------------------------
notes:
	(cd cours/; make info-S1.pdf)

#-------------------------------------------------------------------------------
tdnotes:
	(cd td/; make td-info-S1.pdf)
	(cd td/corriges/; make c-td-info-S1.pdf)

#-------------------------------------------------------------------------------
supports: introductionPaper\
		  instructionsPaper\
		  fonctions-1Paper\
		  fonctions-2Paper\
		  listesPaper

introductionPaper: 
	(cd cours/introduction/; make introductionPaper.pdf)

instructionsPaper: 
	(cd cours/instructions/; make instructionsPaper.pdf)

fonctions-1Paper:
	(cd cours/fonctions/; make fonctions-1Paper.pdf)

fonctions-2Paper:
	(cd cours/fonctions/; make fonctions-2Paper.pdf)

listesPaper:
	(cd cours/listes/; make listesPaper.pdf)

#-------------------------------------------------------------------------------
questions:
	(cd questionnements/; make q-info-S1.pdf)

#-------------------------------------------------------------------------------
ds:
	(cd controles/questionnements/; make all)
	(cd controles/ds/; make all)
	(cd controles/corriges/questionnements/; make all)
	(cd controles/corriges/ds/; make all)
	(cd controles/qcm/; make all)

#-------------------------------------------------------------------------------
plan:
	(cd syllabus/; make info-S1-syllabus.pdf)

#-------------------------------------------------------------------------------
mvrpaper:
	(cd mvr/; make mvr-paper.pdf)

#-------------------------------------------------------------------------------
clean:
	(cd cours/introduction/; make clean)
	(cd cours/instructions/; make clean)
	(cd cours/fonctions/; make clean)
	(cd cours/listes/; make clean)
	(cd cours/; make clean)
	(cd td/; make clean)
	(cd td/corriges/; make clean)
	(cd questionnements/; make clean)
	(cd syllabus/; make clean)
	(cd controles/questionnements/; make clean)
	(cd controles/ds/; make clean)
	(cd controles/corriges/questionnements/; make clean)
	(cd controles/corriges/ds/; make clean)
	(cd controles/qcm/; make clean)
	(cd mvr/; make clean)


