# soundSorter

I made this program to make the process of organizing my splice sample library substantially easier.

There are two key file paths to consider:

1) The path to the directory that splice sends your downloaded samples to
2) The path to the directory that your Digital Audio Workstation accesses, in order to display your sample library

In my case, the path stored as string dir_path correlates to #1, and the path stored as string tar_path correlates to #2.

IMPORTANT: In order for this to work, I made sure that tar_path(file path #2 listed above) leads to a directory filled with
folders designated for each sample category I wanted to have my samples placed into

EXAMPLE:
/Samples
  /drums
  /instrumentals
  /vocals

The program begins by storing the names of a directory into a dictionary, and then asking you to type out the keywords that
you expect the samples meant for this directory to have in their names. 

After this step is done, there will be a dictionary that looks like this:

{
  Vocals: [vocal, spoken, word, rap, freestyle]
  Guitar: [guitar, acoustic_guitar, electric_guitar]
  FX: [cinema, background, rain, rainforest]
}

So if a sample is title: "swift_vocal.wav" 
it should theoretically go into the subfolder titled "vocals" because "vocal" is in the sample name,
and "vocal" is a keyword in the vector-value that is associated with the key called "Vocals"

Next, the program will cycle through every sample that is stored in the path that splice sends your downloaded samples to.
It will create another dictionary, this time the key will be a string representing the sample name, and the value
will be a string representing the full path to the sample, including subdirectories and all, because this is necessary during
the next step, which will copy the sample from its original address to its new address.

An example of what a key-value pairing in this dictionary will look like is this:

{
  "swift_vocal": "/Users/You/Desktop/sounds/packs/swiftFX/swift_vocal.wav"
}

Finally, the program will iterate through the dictionary I just mentioned, and in a nested loop,
iterate through the other dictionary containing the directory, and the vector-value storing the keywords, and in another
nested loop, iterate through the keywords in that vector-value storing the keywords.

So for each sample, if a keyword is in it, the sample is then copied into the directory that is associated with the key connected
to the vector that a match was found in.

Since drums tend to need more sub folders, I specifically added these cases into this step in the code.

JLang






