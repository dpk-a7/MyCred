# MyCred
## A Credential folder protector


A program to hide and unhide your important credential folder completely plus encrypt and decrypt the files present in the folder at the same time, All done by CLI command! Project written in Python.

- Create Key
- Run specific CLI command 
- ✨Magic ✨

## Features

- Hide Folder completely and Encrypt all data present in the folder.
- Unhide Folder and Decrypt all data present in the folder
- List the data present in the folder after hiding
- Create new Folder
- Remove Folder completely! without moving to recycle bin.

To get strarted:
> Step 1 : Install the packages present in requirements.txt
> Step 2 : Create a Key for Encryption and Decrytion by running the following command below
```sh
   py keyGenerator.py
```
This will create a key:
![image](https://user-images.githubusercontent.com/55245100/112860213-3ebbed00-90d1-11eb-915a-92856e097965.png)
And,
You are Ready for protecting your folder

## Commands
![image](https://user-images.githubusercontent.com/55245100/112858865-e9331080-90cf-11eb-8cf8-55750fd5ece1.png)
> (py or python)
> py myCred.py -h : Help
> py myCred.py -hd <folder name> : Hide and Encrypt the folder
> py myCred.py -uh <folder name> : Unhide and Decrypt the folder
> py myCred.py -ls <folder name> : List data present in the folder
> py myCred.py -m <folder name>  : Make new folder
> py myCred.py -r <folder name>  : Remove folder completely


## Example 
I have a folder name web 
![image](https://user-images.githubusercontent.com/55245100/112860759-bb4ecb80-90d1-11eb-824d-cff944c661ff.png)
![image](https://user-images.githubusercontent.com/55245100/112860902-e6391f80-90d1-11eb-9f47-02478d76ceb0.png)
### Hide and encrypt:
```sh
py myCred.py -hd web
```
Now when you refresh, the folder is gone!(its hidden)!
It will not be visible even when view hidden is on:
![image](https://user-images.githubusercontent.com/55245100/112861387-5f387700-90d2-11eb-96cd-85b1518b20ba.png)

And is accessible from search bar:
but all files are Encrypted! :)
![image](https://user-images.githubusercontent.com/55245100/112861599-8ee77f00-90d2-11eb-8e7f-888d305f4466.png)

### List files present in hidden folder:
```sh
py myCred.py -ls web
```
![image](https://user-images.githubusercontent.com/55245100/112862188-23ea7800-90d3-11eb-976c-028346a44b26.png)

### Unhide and Decrypt:
```sh
py myCred.py -hd web
```
### Remove folder:
```sh
py myCred.py -r web
```

> Note: `myCread.py` may not work for other OS as it uses window's command to hide and unhide folder.
You can change the command in `myCred.py`

## License

MIT

**Free Project, Hell Yeah!**
