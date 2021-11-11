const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES]})

const keepMisatoAlive = require("./server")

const config = require("./config.json");
 
let days = [false, false, false, false, false, false, false];
 
const sendDay = () => {
    switch (new Date().getDay()) {
        case 0:
          // if (!days[0]) client.channels.cache.get(config.channel).send(config.sunday);
            days[0] = true;
            break;
        case 1:
            if (!days[1]) client.channels.cache.get(config.channel).send(config.monday);
            days[1] = true;
            break;
        case 2:
        //  if (!days[2]) client.channels.cache.get(config.channel).send(config.tuesday);
            days[2] = true;
            break;
        case 3:
        //  if (!days[3]) client.channels.cache.get(config.channel).send(config.wednesday);
            days[3] = true;
            break;
        case 4:
        //  if (!days[4]) client.channels.cache.get(config.channel).send(config.thursday);
            days[4] = true;
            break;
        case 5:
        //  if (!days[5]) client.channels.cache.get(config.channel).send(config.friday);
            days[5] = true;
            break;
        case 6:
        //  if (!days[6]) client.channels.cache.get(config.channel).send(config.saturday);
            days[6] = true;
            setTimeout(() => {days = [false, false, false, false, false, false, false];}, 600000);
            break;
    }
    setInterval(sendDay, ((60 * 60) * 24) * 1000);
}
 
const wait = () => {
    let now = (new Date().getSeconds() + (new Date().getMinutes() * 60) + (new Date().getHours() * 60 * 60)) * 1000;
    let then = (config.seconds + (config.minutes * 60) + (config.hours * 60 * 60)) * 1000;
    let difference = then - now;
    if (difference < 0) {
        difference += 60 * 60 * 24 * 1000;
    }
    console.log(difference);
    setTimeout(sendDay, difference);
}
 
client.once("ready", () => {
    console.log("Ready!");
    wait();
});
 

keepMisatoAlive()
client.login(config.token);