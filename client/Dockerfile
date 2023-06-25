FROM node:16

WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json
COPY tsconfig.json tsconfig.json
COPY vite.config.ts vite.config.ts

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]