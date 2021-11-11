const express= require("express")

const server = express()

server.all("/", (req,res) => {
  res.send("Misato is running !")
})

function keepMisatoAlive() {
  server.listen(3000, () => {
    console.log("Server ready mate !")
  })
}

module.exports = keepMisatoAlive