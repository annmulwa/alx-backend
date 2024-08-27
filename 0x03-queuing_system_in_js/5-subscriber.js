#!/usr/bin/yarn dev

import { createClient } from "redis";

const client = createClient();
const EXIT_MESSAGE = 'KILL_SERVER';

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (_err, msg) => {
    console.log(msg);
    if (msg == EXIT_MESSAGE) {
        client.unsubscribe();
        client.quit();
    }
});
