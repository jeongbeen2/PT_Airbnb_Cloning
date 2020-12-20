module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [],
  theme: {
    extend: {
      spacing:{
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh",
      },
    },
  },
  variants: {},
  plugins: [],
}

/* #20.4 >> "25vh": "25vh"에서, 왼쪽은 class name, 오른쪽은 css 항목이다. */