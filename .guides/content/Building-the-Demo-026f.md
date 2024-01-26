----------

## Building the Demo

Instruction through Codio is built around the guides feature. This is a brief description on how the demo on the previous page was built. Please see the [documentation](https://docs.codio.com/authoring.html) for more information about content authoring with guides.

||| info
### To try this out
You’ll need to be in Edit Mode. From the top tool bar menu, select  **Tools->Guide->Edit**.


![Selecting Tools->Guide->Edit from the file tree](.guides/img/editGuide.png)
|||

### Page Layout
Each page in the guide can have its own layout. You can select how many panels you want, and what information goes in each panel. The most common layout is two panels without the tree. The guide is in one panel and the code editor is in the other. Click the wrench in the top-right corner of Codio. You can select the layout from here. The default layout is copy the previous page, and Codio does not close any open tabs. Placing the guide on the left allows you to decrease the size of the guide window and leave plenty of room on the right for the Scratch stage.

![Select 2 panels under the label "Layout"](.guides/img/layout.png)

It is a good idea to explicitly state the layout you want. Closing tabs from previous pages also keeps the UI free from unnecessary clutter.

### Code Editor
To use the Scratch editor, add a Scratch file to your project (must have an .sb3 extension). Right-click on the name of your project or book in the directory tree on the left. Select `New File...` and then type its name and file extension.

![In the New File dialog you enter the file name under the label File Name](.guides/img/create_new_file.png)

The next step is to load this file into a panel of your layout. Click on the Guide Editor tab, click on the wrench icon again, and click on the `Open Tabs` button. You can click the button and type the file's path to add a new file to the layout. Or, you can drag the file from the directory tree onto the page. Since your Scratch file will be on the right, you need to change the panel value to 1.

If you want to use a project you have already created on the web version of Scratch, open the project in Scratch and select **File > Save** to your computer, then in Codio select **File > Upload** and open the Scratch file you downloaded. The process is similar for moving Scratch files from Codio to Scratch, ctrl-click on the .sb3 file in Codio and select Download. Then in a new project in Scratch, select **File > Load** from your computer.


This file will open with the guide. The file will remain opened until the student closes the tab. This is why it is a good idea to tell Codio to close any previously opened tabs when selecting the layout.

### Markdown
Guides are authored with [markdown](https://docs.codio.com/instructors/authoring/guides/markdown_content.html#markdown), but you can use any HTML to author content. 

### Images
You will notice a folder called `.guides` in the directory tree. To view the File Tree, select **View->File Tree**. All of the information in this folder is hidden from students. There is a subfolder called `img` where you can upload any images you want to appear in the guide. Right-click on the `img` folder and select `Upload...`.

![Selecting upload after ctrl-clicking or Right-clicking on the img folder.](.guides/img/upload.png)

Add the image to the guide using markdown syntax.
