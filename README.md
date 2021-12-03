# Quantum_Entanglement_Experiments_Arduino_Python
A series of codes for conducting the quantum entanglement experiments as showcased on my YouTube Channel. Using a non-linear crystal made of Beta-Barium Borate (BBO) I am able to generate 2 entangled photon beams of wavelength 810nm each from a pump laser beam of 405nm which is pulsed using the Arduino and directed into the splitter. the entangled photons are in quantum superposition of the H and V modes, with the indeterminacy being a perfect 50/50 split. These are directed by beamsplitters into 2 detectors which either detect a H or V mode but never both. Whichever silicon phototransistor sensor on the arduino detects the H and which detects the V mode is purely random creating a random number source that is irreducible and thus unhackable. The random numbers generated by this scheme are a stream of integer bits. To generate purely random non-integers I use a CCD and a split mirror that directs the 2 photons into an aperture of a connected CCD microscope sensor. By splitting the image were the 2 beams of entangled photons meet and correlating the 2 images to detect random changes we can assume due to the nature of entanglement that the difference between the images must be in part due to the random fluctuations of the vacuum as the 2 entangled photons when cross-correlated should be equal but of opposite polarization. the randomness is beneath the intrinsic shot noise of the CCD sensor as quantum entangled photon streams generated in such a scheme allow for sub-shot noise imaging in holography setups. A python code for generating cross-correlated images is also available to use in this repository however it requires time to correlate across all the pixel data. this can be used as a way to produce sub-shot noise images using standard CCD microscope cameras in such a setup.
