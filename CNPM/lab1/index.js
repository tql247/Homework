const { app, BrowserWindow, Menu } = require('electron')
const { ipcMain } = require('electron')
const dialog = require('electron').dialog
const fs = require("fs")
const path = require('path')
// var request = require('request')


// DATAFILE = '/data/data.json'
// DATAFILE = path.join(__dirname, DATAFILE);
// USER = ''
// TOKEN = ''


function createWindow () {
  // Create the browser window.
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true
    },
    resizable: false
  })

  // Build menu
  const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
  // Insert menu
  Menu.setApplicationMenu(mainMenu)

  // and load the index.html of the app.
  win.loadFile('views/index.html')

  // call loggin api
  // ipcMain.handle('login', (event, ...args) => {})
  

  // Open the DevTools.
  win.webContents.openDevTools()
}


const mainMenuTemplate = [
    // {
    //     label: 'File',
    //     submenu: [
    //         {
    //             label: 'Add Item'
    //         }
    //     ]
    // }
]

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(createWindow)

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
