# quilt-square-randomizer
python script, generates a randomly-ordered list of coordinates

# Usage
1. clone/download to a folder on your computer
2. make the shell script executable
3. run it
4. read the new quilt-coordinates.txt file for your results

from linux/macos terminal:

```bash
> git clone https://github.com/druidgreeneyes/quilt-square-randomizer
...
> cd quilt-square-randomizer
> chmod +x quilt-coordinates.sh
> ./quilt-coordinates.sh 20 26
> nano quilt-coordinates.txt
```

every time you run it, it will replace the existing quilt-coordinates.txt file, so make a backup copy before you start using a given result:

```bash
> cp quilt-coordinates.txt my-quilt-coordinates.txt
```
