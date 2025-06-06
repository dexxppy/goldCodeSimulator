document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (e) {
        const sentToTransmit = this.sent_to_transmit.value.trim();
        const runs = parseInt(this.runs.value);
        const degreeN = parseInt(this.degree_n.value);
        const seed1 = this.seed1.value.trim();
        const seed2 = this.seed2.value.trim();

        const errors = [];

        if (!/^[a-zA-Z0-9]+$/.test(sentToTransmit)) {
            errors.push("Sent to transmit can only contain letters and digits.");
        }

        if (isNaN(runs) || runs < 1 || runs > 100) {
            errors.push("Runs must be a number between 1 and 100.");
        }

        if (!isNaN(degreeN)) {
            if (degreeN < 5 || degreeN > 11 || degreeN === 8) {
                errors.push("Degree n must be between 5 and 11, excluding 8.");
            }
        }

        if (seed1 || seed2) {
            if (!/^[01]*$/.test(seed1) || !/^[01]*$/.test(seed2)) {
                errors.push("Seeds must contain only 0 and 1.");
            }
            if (seed1.length !== seed2.length) {
                errors.push("Seed1 and Seed2 must be of the same length.");
            }
            if (!isNaN(degreeN) && seed1.length !== degreeN) {
                errors.push("Seed1 and Seed2 length must equal degree n.");
            }
        }

        if (errors.length > 0) {
            e.preventDefault();
            alert(errors.join("\n"));
        }
    });
});
