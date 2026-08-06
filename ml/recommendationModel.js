const { RandomForestClassifier } = require('ml-random-forest');
const dataset = require('./dataset');

const X = dataset.map((d) => [
    d.similarity,
    d.price,
    d.type,
    d.queryLength,
    d.titleLength,
]);

const Y = dataset.map((d) => d.label);

const options = {
    nEstimators: 100,
    maxFeatures: 1.0,
    replacement: true,
    seed: 42,
};

const classifier = new RandomForestClassifier(options);

classifier.train(X, Y);

function predict(features) {
    const input = [
        [
            features.similarity,
            features.price,
            features.type === 'PAID' ? 1 : 0,
            features.queryLength,
            features.titleLength,
        ],
    ];

    const prediction = classifier.predict(input)[0];
    console.log("Features:", features);
    console.log("Prediction:", prediction);


    const confidence =
        prediction === 1
            ? 0.9
            : 0.3;

    return confidence;
}

module.exports = {
    predict,
};
