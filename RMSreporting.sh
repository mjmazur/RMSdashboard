#!/bin/bash
# This is taken from the original iStream shell scrip
echo ""
echo "START EXTERNAL SCRIPT..." 
echo ""
echo "CHECKING ARGUMENTS..."
echo ""
if [[ -z "$1" || -z "$2" || -z "$3" || -z "$4" || -z "$5" || -z "$6" || -z "$7" || -z "$8" || -z "$9" ]]; then
	echo "MISSING ARGUMENTS..."
	echo "EXIT..."
	echo ""	
	exit
fi


echo "CHECKING DEPENDENCIES"
if [[ ( $( command -v ffmpeg ) ) && $( command -v convert ) ]]; then
        echo "ALL DEPENDENCIES ALREADY INSTALLED!"
else
	if $( sudo -n true ) ; then
        echo "INSTALLING DEPENDENCIES..."
        sudo apt-get update
        sudo apt-get -y install imagemagick 
        sudo apt-get -y install ffmpeg
	sudo apt-get -y install curl
    else
    	echo "NO SUDO PRIVILEDGES TO INSTALL DEPENDENCIES..."
    fi
fi


# If avconv is not available, set up an alias for ffmpeg
if [ ! $( command -v avconv ) ]; then
	alias avconv="ffmpeg"
fi

###SETUP###
SYSTEM="RMS"
STATION_ID=$1
CAPTURED_DIR_NAME=$2
ARCHIVED_DIR_NAME=$3
LATITUDE=$4
LONGITUDE=$5
ELEVATION=$6
WIDTH=$7
HEIGHT=$8
REMAINING_SECONDS=$9

echo "REMAININS SECONDS = $REMAINING_SECONDS"
echo ""

LEVEL_1_SECONDS=3600 # 60 min => all files
LEVEL_2_SECONDS=1800 # 30 min => without captured_stack
LEVEL_3_SECONDS=300 # 5 min => without captured_stack and without timelapse_video
LEVEL_1=false
LEVEL_2=false
LEVEL_3=false

if [ "$REMAINING_SECONDS" -lt "$LEVEL_2_SECONDS" ]; then
	LEVEL_3=true
	ACTIVE_LEVEL=3
elif [ "$REMAINING_SECONDS" -lt "$LEVEL_1_SECONDS" ]; then
	LEVEL_2=true
	ACTIVE_LEVEL=2
elif [ "$REMAINING_SECONDS" -ge "$LEVEL_1_SECONDS" ]; then
	LEVEL_1=true
	ACTIVE_LEVEL=1
fi

echo "ACTIVE_LEVEL = $ACTIVE_LEVEL"
echo ""

DATE_NOW=$(date +"%Y%m%d")
TMP_VIDEO_FILE="$CAPTURED_DIR_NAME/$(basename $CAPTURED_DIR_NAME).mp4"
VIDEO_FILE="$CAPTURED_DIR_NAME/${STATION_ID}_${DATE_NOW}.mp4"
SMALL_VIDEO_FILE="$CAPTURED_DIR_NAME/$(basename $CAPTURED_DIR_NAME)_timelapse.mp4"
AGENT="$SYSTEM-$STATION_ID"
FTP_DETECT_INFO="$(ls $CAPTURED_DIR_NAME/*.txt | grep 'FTPdetectinfo' | grep -vE "uncalibrated")"

#Thanks to Alfredo Dal'Ava Junior :)
if [[ -z "$FTP_DETECT_INFO" ]]; then
   METEOR_COUNT="0"
else
   METEOR_COUNT="$(sed -n 1p $FTP_DETECT_INFO | awk '{ print $NF }')"
fi

function generate_captured_stack {	
	if ($LEVEL_1); then
		cd ~/source/RMS
		python -m Utils.StackFFs $CAPTURED_DIR_NAME bmp -s -x
	fi
}

function generate_timelapse {
	SECONDS_LIMIT=$(expr $REMAINING_SECONDS - 120)
	if ($LEVEL_1); then
		cd ~/source/RMS
		python -m Utils.GenerateTimelapse $CAPTURED_DIR_NAME
		mv $TMP_VIDEO_FILE $VIDEO_FILE
		ffmpeg -i $VIDEO_FILE -vf scale="720x480" $SMALL_VIDEO_FILE
	fi
	if ($LEVEL_2); then
		cd ~/source/RMS
		python -m Utils.GenerateTimelapse $CAPTURED_DIR_NAME
		mv $TMP_VIDEO_FILE $VIDEO_FILE
		ffmpeg -i $VIDEO_FILE -vf scale="720:480" $SMALL_VIDEO_FILE
	fi
}

VAR_1="1"
VAR_2="1"

if [ $VAR_1 = $VAR_2 ]; then	
	echo "GENERATE FULL NIGHT STACK..."
	generate_captured_stack
	echo ""

	# echo "GENERATE VIDEO..."
	# generate_timelapse
	# echo ""
fi
echo "END EXTERNAL SCRIPT..."
echo ""
