/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        '../../**/templates/*.html',
        '!../../**/node_modules',
        '../../**/*.js',
        '../../**/*.py'
    ],
    safelist: [
    ],
    corePlugins: {
        container: false,
        },
        theme: {
        borderRadius: {
            'DEFAULT': '32px',
            'none': '0',
            'sm': '8px',
            'sm-inner': '7px',
            'full': '9999px',
        },
        aspectRatio: {
            'square': '1/1',
        },
        colors: {
            'transparent': 'transparent',
            'current': 'currentColor',
            'black': {
                DEFAULT: '#000',
                100:  '#999',
                200: '#d8d8da',
                400: '#acacac',
                500: '#797979',
                600: '#535353',
                700: '#4a4a4a',
                800: '#313131',
            },
            'blue': {
                DEFAULT: '#02143f',
                50: '#f2f5f9',
                100: '#e6ecf8',
                200: '#d6dcf2',
                300: '#b9c6f4',
                400: '#A4C3E0',
                500: '#8EB0CC',
                600: '#759CC1',
                800: '#1C3981',
                900: '#051E57',
            },
            'green': {
                DEFAULT: '#20bf55',
                500: '#009f5a',
            },
            'muted': '#8d8d8d',
            'red': '#e50a19',
            'white': '#fff',
            'yellow': '#F9DB6D',
        },
        listStyleType: {
            none: 'none',
            disc: 'disc',
            decimal: 'decimal',
        },
        fontFamily: {
            sans: ['"Source Sans 3"', 'sans-serif'],
        },
        extend: {
            inset: {
                '50vw': '-50vw',
            },
            height: {
                'font': '0.9em',
            },
            maxWidth: {
                'sm': '12rem',
                '2xl': '42rem', //672px
                '3xl': '48rem', //768px
                '4xl': '56rem', //896px
                '5xl': '64rem', //1024px
                '6xl': '72rem', //1152px
                '7xl': '80rem', //1280px
                '8xl': '88rem', //1408px
            },
            width: {
                'font': '0.9em',
            },
            borderWidth: {
                'grid-table': '0.5px',
            },
            gridTemplateColumns: {
                '15': 'repeat(15, minmax(0, 1fr))',
            },
            spacing: {
                '30': '7.5rem',
            },
            backgroundImage: {
                'city': 'url(/static/pexels-caio-11331744.jpg)',
            },
            fontSize: {
                '0': '0',
                'h1': ['30px', {
                    lineHeight: '1.0125',
                }],
                'h1-p': ['24px', {
                    lineHeight: '1.0125',
                }],
                'h2': ['24px', {
                    lineHeight: '1.0125',
                }],
                'h2-p': ['18px', {
                    lineHeight: '1.0125',
                }],
                'sm': ['14px', {
                    lineHeight: '1.4375',
                }],
                'md': ['16px', {
                    lineHeight: '1.5',
                }],
                'lg': ['20px', {
                    lineHeight: '1.5',
                }],
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}