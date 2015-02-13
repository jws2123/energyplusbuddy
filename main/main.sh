#!/bin/sh

# Start by creating all of the IDF files 


echo 'Creating IDF files...'
python ./../combinations/combinatorics.py
echo 'DONE'

echo 'Running energy models. This may take a while...'

# Figure out how many processors are available

PROC=$(nproc)

# Start a tmux session

SESSION=$USER
tmux -2 new-session -d -s $SESSION  	# -2 forces tmux to assume the terminal supports 256 colors.
					# -d detaches the session
					# -s names the session

# Create a new window
tmux new-window -t $SESSION:1 -n 'Models'  # -t specifies a target, -n names the window?

# split the window into 8 panes.  
# TODO: add windows so that the number of panes on a window does not exceed 8?

tmux split-window -h #splits the window horizontally 
tmux select-pane -t 1 #ensures we are selecting pane 1, not 0.  needed?
tmux split-window -v #splits the window vertically 
tmux select-pane -t 2 #ensures we are selecting pane 2, not 1.  needed?
tmux split-window -v
tmux select-pane -t 1 #needed
tmux split-window -v
tmux select-pane -t 0 #needed
tmux split-window -v
tmux select-pane -t 5 #needed?
tmux split-window -v
tmux select-pane -t 0 #needed
tmux split-window -v 

echo 'Done initializing tmux session and setting up windows'



idfs=(./idfs/[0-9]*.idf)

for ((i=0; i<${#idfs[@]}; i++))
do
	PANE=$((i%8))
	tmux select-pane -t $PANE
	tmux send-keys "runEP$PANE ${idfs[$i]} USA_NY_New.York-J.F.Kennedy.Intl.AP.744860_TMY3.epw" C-m
 
done

#Set-up an extra window
tmux new-window -t $SESSION:2 -n 'Play_while_you_work'
tmux send-keys "echo Energy Models are running in window 1" C-m

echo 'DONE'

#Set default window
tmux select-window -t $SESSION:2


#Attach to session
tmux -2 attach-session -t $SESSION

