# Appendix  
# Explanation of the Adversarial Evolution Simulation Program  

This program can, to a certain extent, reflect the intrinsic laws governing human origins and the rise and fall of empires. Its basic workflow is as shown below:  

### Basic Fitness  
Basic Fitness refers to fitness in the context of narrow-sense natural selection.  
#  
From top to bottom, each genetic strategy imposes increasing demands on the brain, and their narrow-sense natural fitness decreases accordingly (assuming the brain is used solely for the operation of genetic strategies).  
Gene_Strategy_Fitness_Table = {  
    'Concern_Only_Oneself': 1,  #  
    In the absence of inter-biological cooperation or grabbing, organisms require almost no complex brain.  
    'Altruism': 0.98,  #  
    Pure reciprocity is unconditional, so no brain is needed for judgment.  
    'Gangster': 0.93,  #  
    Grabbingism requires a brain to command prey capture, creating the initial demand for the brain (an internal cause of the Cambrian Explosion).  
    'Tit_For_Tat': 0.8,  #  
    The Tit-for-Tat mechanism requires a brain to judge which individuals are beneficial or harmful to itself (a significant driver of brain evolution).  
    'GVBE_1': 0.6,  #  
    First-order Virtue-Upholding and Evil-Rejectionism requires a more advanced brain and memory for virtue-evil quantification and memory, further increasing brain demands (a key reason for accelerated brain evolution).  
    'Hypocrisy_1': 0.57,  #  
    First-order Hypocrisyism needs to deceive first-order Virtue-Upholding and Evil-Rejectionism, conceal its actions while engaging in grabbing, imposing even greater demands on the brain.  
    'GVBE_2': 0.55,  #  
    Second-order Virtue-Upholding and Evil-Rejectionism can detect the disguises of first-order Hypocrisyism on the basis of first-order Virtue-Upholding and Evil-Rejectionism, further increasing brain demands.  
    'Hypocrisy_2': 0.52,  #  
    Second-order Hypocrisyism can deceive second-order Virtue-Upholding and Evil-Rejectionism on the basis of first-order Hypocrisyism, further increasing brain demands.  
    'GVBE_3': 0.5,  #  
    Third-order Virtue-Upholding and Evil-Rejectionism can detect the disguises of second-order Hypocrisyism on the basis of second-order Virtue-Upholding and Evil-Rejectionism, further increasing brain demands.  
    'Hypocrisy_3': 0.47,  #  
    Third-order Hypocrisyism can deceive third-order Virtue-Upholding and Evil-Rejectionism on the basis of second-order Hypocrisyism, further increasing brain demands.  
#  
Generally, deception is more difficult than detection. Throughout human history, Virtue-Upholding and Evil-Rejectionism often struggles to advance, leading to cycles of grabbing.  
}  

### Adversarial Evolution  
def meetWithOtherCreature(self, other, grid):  
This function primarily simulates the interaction process of different genetic types within a grid (the process of Adversarial Evolution). This process is roughly as shown in the table below:  
——————————————————————————————————————————————  
                COO        Altruism   Gangster   TFT        GVBE_1       Hypocrisy_1   GVBE_2       Hypocrisy_2   GVBE_3       Hypocrisy_3  
——————————————————————————————————————————————  
  COO           Pass       Pass       Pass       Pass       Pass         Pass          Pass         Pass          Pass         Pass  
  Altruism      Altruism   Altruism   Altruism   Altruism   Altruism     Altruism      Altruism     Altruism      Altruism     Altruism  
  Gangster      Rob        Rob        Rob        Rob        Rob          Rob           Rob          Rob           Rob          Rob  
  TFT           Pass       Altruism   Rob        Altruism   Altruism     Altruism      Altruism     Altruism      Altruism     Altruism  
  GVBE_1        Pass       Altruism   Punish     Altruism   AltruismX2   AltruismX2    AltruismX2   AltruismX2    AltruismX2   AltruismX2  
  Hypocrisy_1   Rob        Rob        Rob        Altruism   Rob          Rob           Rob          Rob           Rob          Rob  
  GVBE_2        Pass       Altruism   Punish     Altruism   AltruismX2   Punish        AltruismX2   AltruismX2    AltruismX2   AltruismX2  
  Hypocrisy_2   Rob        Rob        Rob        Altruism   Rob          Rob           Rob          Rob           Rob          Rob  
  GVBE_3        Pass       Altruism   Punish     Altruism   AltruismX2   Punish        AltruismX2   Punish        AltruismX2   AltruismX2  
  Hypocrisy_3   Rob        Rob        Rob        Altruism   Rob          Rob           Rob          Rob           Rob          Rob  
——————————————————————————————————————————————  
Note: COO = Concern Only Oneself; TFT = Tit For Tat; GVBE = Good for Virtue, Bad for Evil; AltruismX2 = Altruistic Behavior with Sacrificial spirit  

### Main Conclusions:  
Different from the Tit-for-Tat strategy defined on the basis of the traditional Prisoner’s Dilemma, the Tit-for-Tat mechanism in this model is not fully evolutionarily stable even before the emergence of Virtue-Upholding and Evil-Rejectionism. It can be disrupted by pure Altruism (previous models did not account for the fact that the brain investment required for Tit-for-Tat is significantly higher than that for unconditional Altruism).  

<p align="center"></p>  
Humanity originated from Virtue-Upholding and Evil-Rejectionism evolving from the Tit-for-Tat mechanism.  

<p align="center"></p>  
Even if Virtue-Upholding and Evil-Rejectionism individuals emerge through multiple mutations, they will be quickly eliminated if their scale is small.  

<p align="center"></p>  
Virtue-Upholding and Evil-Rejectionism individuals only enter a phase of explosive growth when they reach a certain scale, which closely resembles human evolutionary history—human’s close species all failed and declined to varying degrees, while humans achieved enormous success in a short period (the Great Leap Period).  

<p align="center"></p>  
Before the emergence of Hypocrisyism, Virtue-Upholding and Evil-Rejectionism can enter an evolutionarily stable state with unprecedented prosperity (the Edenic Period). However, the appearance of Hypocrisyism will rapidly disintegrate the Virtue-Upholding and Evil-Rejectionism group.  

<p align="center"></p>  
Hypocrisyism is not evolutionarily stable. It is more akin to cancer cells: after disintegrating the Virtue-Upholding and Evil-Rejectionism group it parasitizes, it is swiftly eliminated by more overt Grabbingism. Hypocrisyism bullies the virtuous and fears the evil, leading to the phenomenon of progressive grabbing, and the group degenerates back into the "Hobbesian Jungle."  

<p align="center"></p>  
The cycle of imperial rise and fall is essentially a cycle of Grabbingism—Tit-for-Tat (Altruism)—Virtue-Upholding and Evil-Rejectionism—Hypocrisyism—Grabbingism.  

<p align="center"></p>  
When Virtue-Upholding and Evil-Rejectionism genes migrate to regions dominated by Grabbingism, they will rapidly thrive. Meanwhile, old regions dominated by Virtue-Upholding and Evil-Rejectionism are prone to more Hypocrisyism due to excessive prosperity. Consequently, marginal empires rise while established empires decline. This results in alternating cycles of rise and fall among empires in different regions. For example:  
> <p align="center"></p>  
After a period, an empire in the top-left corner enters a decline due to the emergence of many hypocrites, while empires in the bottom-left and bottom-right corners enter a period of rise.  
> <p align="center"></p>  
Another example: an empire in the bottom-right corner rises first.  
<p align="center"></p>  
When it declines due to hypocrites, other empires in different regions thrive because of the migrated Virtue-Upholding and Evil-Rejectionism individuals.  

<p align="center"></p>