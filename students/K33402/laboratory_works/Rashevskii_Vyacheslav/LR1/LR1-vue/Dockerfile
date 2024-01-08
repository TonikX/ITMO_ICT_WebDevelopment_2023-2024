FROM node:10-alpine

WORKDIR /LR1-vue
COPY package.json .
RUN npm install
RUN npm i muse-ui -S
RUN npm install --save-dev @babel/preset-env
COPY . /LR1-vue
EXPOSE 8080
CMD ['npm', 'start']