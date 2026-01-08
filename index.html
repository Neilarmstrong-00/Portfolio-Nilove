<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nilove Mandal | Kinetic Blueprint Portfolio</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Three.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Tailwind Config for Custom Colors/Fonts -->
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        blueprint: {
                            900: '#0a0a0f', // Deepest background
                            800: '#121218', // Card background
                            700: '#1c1c26', // Border
                            500: '#2d3e50', // Grid lines
                        },
                        neon: {
                            cyan: '#00f0ff',
                            orange: '#ff5e00',
                            green: '#0aff0a'
                        }
                    },
                    backgroundImage: {
                        'grid-pattern': "linear-gradient(to right, #2d3e501a 1px, transparent 1px), linear-gradient(to bottom, #2d3e501a 1px, transparent 1px)",
                    }
                }
            }
        }
    </script>

    <style>
        /* Base Styles */
        body {
            background-color: #0a0a0f;
            color: #e2e8f0;
            overflow-x: hidden;
        }

        /* Blueprint Grid Background */
        .bg-blueprint-grid {
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(45, 62, 80, 0.1) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(45, 62, 80, 0.1) 1px, transparent 1px);
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0a0a0f; 
        }
        ::-webkit-scrollbar-thumb {
            background: #2d3e50; 
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #00f0ff; 
        }

        /* X-Ray / Wireframe Mode Classes */
        body.wireframe-mode .project-card {
            background: rgba(10, 10, 15, 0.7);
            border: 1px dashed #00f0ff;
            box-shadow: none;
        }
        
        body.wireframe-mode .project-image {
            filter: grayscale(100%) contrast(1.2) brightness(0.8);
            opacity: 0.8;
            border-bottom: 1px dashed #00f0ff;
        }

        body.wireframe-mode .accent-text {
            color: #00f0ff !important;
            text-shadow: 0 0 5px rgba(0, 240, 255, 0.5);
        }

        body.wireframe-mode .btn-primary {
            background: transparent;
            border: 1px solid #00f0ff;
            color: #00f0ff;
        }
        
        body.wireframe-mode .btn-primary:hover {
            background: rgba(0, 240, 255, 0.1);
            box-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
        }

        /* Standard Mode Classes */
        .project-card {
            background: #121218;
            border: 1px solid #1c1c26;
            transition: all 0.3s ease;
        }
        .project-card:hover {
            border-color: #2d3e50;
            transform: translateY(-5px);
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        }

        /* Utilities */
        .tech-tag {
            font-size: 0.75rem;
            padding: 2px 8px;
            border-radius: 4px;
            font-family: 'JetBrains Mono', monospace;
        }

        .canvas-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            z-index: -1;
            opacity: 0.6;
            pointer-events: none;
        }

        /* Toggle Switch */
        .toggle-checkbox:checked {
            right: 0;
            border-color: #00f0ff;
        }
        .toggle-checkbox:checked + .toggle-label {
            background-color: #00f0ff;
        }
    </style>
</head>
<body class="bg-blueprint-grid min-h-screen relative selection:bg-neon-cyan selection:text-black">

    <!-- 3D Background Canvas -->
    <div id="canvas-container" class="canvas-container"></div>

    <!-- Navigation -->
    <nav class="fixed top-0 w-full z-50 border-b border-blueprint-700 bg-blueprint-900/90 backdrop-blur-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <!-- Brand -->
                <div class="flex items-center">
                    <span class="text-neon-cyan font-mono text-xl font-bold tracking-tighter">&lt;NM /&gt;</span>
                    <span class="ml-3 font-mono text-sm hidden sm:block text-gray-400">NILOVE MANDAL_PORTFOLIO.SYS</span>
                </div>

                <!-- Controls -->
                <div class="flex items-center space-x-6">
                    <!-- X-Ray Toggle -->
                    <div class="flex items-center space-x-2">
                        <span class="text-xs font-mono text-gray-500 uppercase">Render</span>
                        <div class="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in">
                            <input type="checkbox" name="toggle" id="xray-toggle" class="toggle-checkbox absolute block w-5 h-5 rounded-full bg-white border-4 appearance-none cursor-pointer border-gray-300 left-0 transition-all duration-300"/>
                            <label for="xray-toggle" class="toggle-label block overflow-hidden h-5 rounded-full bg-gray-700 cursor-pointer border border-gray-600"></label>
                        </div>
                        <span class="text-xs font-mono text-neon-cyan uppercase">Blueprint</span>
                    </div>
                    
                    <a href="#contact" class="hidden md:inline-block px-4 py-2 border border-neon-orange text-neon-orange font-mono text-xs hover:bg-neon-orange hover:text-black transition-colors uppercase tracking-widest">
                        Contact_Me
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative h-screen flex items-center justify-center overflow-hidden pt-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            
            <div class="space-y-6">
                <div class="inline-block border border-neon-cyan/30 bg-neon-cyan/5 px-3 py-1 rounded text-neon-cyan font-mono text-xs mb-2">
                    System Status: ONLINE // Ready for Hire
                </div>
                <h1 class="text-5xl md:text-7xl font-bold font-sans tracking-tight leading-none text-white">
                    Bridging <span class="accent-text text-gray-400 transition-colors">Digital Design</span> <br/>
                    & <span class="accent-text text-neon-orange transition-colors">Kinetic Reality</span>.
                </h1>
                <p class="text-gray-400 text-lg max-w-lg font-light">
                    I am Nilove Mandal. An engineer who solves problems like "Liquid Slosh Resonance" and "Optical Distortion". I build reliable, modular, and innovative systems.
                </p>
                
                <div class="flex flex-wrap gap-4 pt-4">
                    <a href="#projects" class="btn-primary group relative px-6 py-3 bg-white text-black font-mono font-bold hover:bg-neon-cyan transition-all">
                        VIEW_INVENTIONS
                        <span class="absolute -bottom-2 -right-2 w-full h-full border border-gray-500 group-hover:border-neon-cyan transition-all -z-10"></span>
                    </a>
                    <a href="#skills" class="px-6 py-3 border border-gray-600 text-gray-300 font-mono hover:border-white hover:text-white transition-all">
                        EXPLORE_TOOLKIT
                    </a>
                </div>

                <!-- Stats -->
                <div class="grid grid-cols-3 gap-6 pt-8 border-t border-gray-800">
                    <div>
                        <div class="text-2xl font-mono font-bold text-white">8+</div>
                        <div class="text-xs text-gray-500 uppercase tracking-wider">Prototypes</div>
                    </div>
                    <div>
                        <div class="text-2xl font-mono font-bold text-white">2.97</div>
                        <div class="text-xs text-gray-500 uppercase tracking-wider">Safety Factor</div>
                    </div>
                    <div>
                        <div class="text-2xl font-mono font-bold text-white">100%</div>
                        <div class="text-xs text-gray-500 uppercase tracking-wider">Passion</div>
                    </div>
                </div>
            </div>

            <!-- Hero Visual (Placeholder for 3D interaction zone) -->
            <div class="hidden lg:block h-96 relative">
                 <div class="absolute inset-0 flex items-center justify-center opacity-30 pointer-events-none">
                    <svg class="w-full h-full" viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="200" cy="200" r="150" stroke="#2d3e50" stroke-width="1" stroke-dasharray="4 4"/>
                        <circle cx="200" cy="200" r="100" stroke="#2d3e50" stroke-width="1"/>
                        <line x1="200" y1="0" x2="200" y2="400" stroke="#2d3e50" stroke-width="1"/>
                        <line x1="0" y1="200" x2="400" y2="200" stroke="#2d3e50" stroke-width="1"/>
                    </svg>
                 </div>
                 <!-- Note: Three.js canvas sits behind this -->
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="py-24 relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-16">
                <h2 class="text-neon-orange font-mono text-sm uppercase tracking-widest mb-2">01. Innovation Archive</h2>
                <h3 class="text-4xl font-bold text-white">Featured Inventions</h3>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">

                <!-- Project 1: Vajra 2.0 -->
                <div class="project-card rounded-lg overflow-hidden group relative">
                    <div class="h-64 bg-gray-900 relative overflow-hidden border-b border-gray-800 project-image">
                        <!-- Blueprint Visual Representation -->
                        <div class="absolute inset-0 flex items-center justify-center opacity-20 group-hover:opacity-40 transition-opacity">
                            <svg class="w-32 h-32 text-neon-orange" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                <rect x="2" y="2" width="20" height="20" rx="5" ry="5" stroke-width="1" stroke-dasharray="2 2"/>
                            </svg>
                        </div>
                        <div class="absolute bottom-4 left-4 bg-black/80 px-3 py-1 text-xs font-mono text-neon-orange border border-neon-orange">
                            AGRO-TECH
                        </div>
                    </div>
                    <div class="p-8">
                        <div class="flex justify-between items-start mb-4">
                            <h4 class="text-2xl font-bold text-white group-hover:text-neon-orange transition-colors">Vajra 2.0</h4>
                            <span class="text-gray-500 font-mono text-xs">2024</span>
                        </div>
                        <p class="text-gray-400 mb-6 text-sm leading-relaxed">
                            A teleoperated rover designed to eliminate human exposure to hazardous pesticides. Features a rigid Fixed-Arm Chassis to counteract "sloshing" forces.
                        </p>
                        
                        <div class="border-l-2 border-neon-orange pl-4 mb-6">
                            <p class="text-xs font-mono text-gray-500 uppercase mb-1">Key Achievement</p>
                            <p class="text-sm text-white">Solved "Liquid Slosh Resonance" instability ensuring predictable handling.</p>
                        </div>

                        <div class="flex flex-wrap gap-2">
                            <span class="tech-tag bg-gray-800 text-gray-300">SolidWorks</span>
                            <span class="tech-tag bg-gray-800 text-gray-300">ESP32</span>
                            <span class="tech-tag bg-gray-800 text-gray-300">Teleoperation</span>
                        </div>
                    </div>
                </div>

                <!-- Project 2: Industrial Kuli -->
                <div class="project-card rounded-lg overflow-hidden group relative">
                    <div class="h-64 bg-gray-900 relative overflow-hidden border-b border-gray-800 project-image">
                        <div class="absolute inset-0 flex items-center justify-center opacity-20 group-hover:opacity-40 transition-opacity">
                            <svg class="w-32 h-32 text-neon-cyan" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                            </svg>
                        </div>
                        <div class="absolute bottom-4 left-4 bg-black/80 px-3 py-1 text-xs font-mono text-neon-cyan border border-neon-cyan">
                            LOGISTICS
                        </div>
                    </div>
                    <div class="p-8">
                        <div class="flex justify-between items-start mb-4">
                            <h4 class="text-2xl font-bold text-white group-hover:text-neon-cyan transition-colors">Industrial Kuli</h4>
                            <span class="text-gray-500 font-mono text-xs">2023</span>
                        </div>
                        <p class="text-gray-400 mb-6 text-sm leading-relaxed">
                            Synchronized Crab-Steering AGV using a single-actuator omni-directional design. Reduces actuator count by 75% while maintaining precision.
                        </p>
                        
                        <div class="border-l-2 border-neon-cyan pl-4 mb-6">
                            <p class="text-xs font-mono text-gray-500 uppercase mb-1">Key Achievement</p>
                            <p class="text-sm text-white">&lt;2% error variance in 4-wheel steering synchronization.</p>
                        </div>

                        <div class="flex flex-wrap gap-2">
                            <span class="tech-tag bg-gray-800 text-gray-300">Mechanical Design</span>
                            <span class="tech-tag bg-gray-800 text-gray-300">Hybrid Nav</span>
                            <span class="tech-tag bg-gray-800 text-gray-300">Prototyping</span>
                        </div>
                    </div>
                </div>

                <!-- Project 3: Hootie -->
                <div class="project-card rounded-lg overflow-hidden group relative">
                    <div class="h-64 bg-gray-900 relative overflow-hidden border-b border-gray-800 project-image">
                        <div class="absolute inset-0 flex items-center justify-center opacity-20 group-hover:opacity-40 transition-opacity">
                            <svg class="w-32 h-32 text-purple-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                        </div>
                        <div class="absolute bottom-4 left-4 bg-black/80 px-3 py-1 text-xs font-mono text-purple-400 border border-purple-400">
                            ROBOTICS
                        </div>
                    </div>
                    <div class="p-8">
                        <div class="flex justify-between items-start mb-4">
                            <h4 class="text-2xl font-bold text-white group-hover:text-purple-400 transition-colors">Hootie Robot</h4>
                            <span class="text-gray-500 font-mono text-xs">2023</span>
                        </div>
                        <p class="text-gray-400 mb-6 text-sm leading-relaxed">
                            Biomimetic IoT Companion. Features a screwless snap-fit enclosure and "Chimney Effect" passive cooling system.
                        </p>
                        
                        <div class="border-l-2 border-purple-400 pl-4 mb-6">
                            <p class="text-xs font-mono text-gray-500 uppercase mb-1">Key Achievement</p>
                            <p class="text-sm text-white">Seamless transition between "Autonomous Life" and "Puppeteer Mode".</p>
                        </div>

                        <div class="flex flex-wrap gap-2">
                            <span class="tech-tag bg-gray-800 text-gray-300">C++</span>
                            <span class="tech-tag bg-gray-800 text-gray-300">Animatronics</span>
                            <span class="tech-tag bg-gray-800 text-gray-300">3D Printing</span>
                        </div>
                    </div>
                </div>

                <!-- Project 4: Smart Breathe -->
                <div class="project-card rounded-lg overflow-hidden group relative">
                    <div class="h-64 bg-gray-900 relative overflow-hidden border-b border-gray-800 project-image">
                        <div class="absolute inset-0 flex items-center justify-center opacity-20 group-hover:opacity-40 transition-opacity">
                             <svg class="w-32 h-32 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                            </svg>
                        </div>
                        <div class="absolute bottom-4 left-4 bg-black/80 px-3 py-1 text-xs font-mono text-green-500 border border-green-500">
                            MEDICAL IOT
                        </div>
                    </div>
                    <div class="p-8">
                        <div class="flex justify-between items-start mb-4">
                            <h4 class="text-2xl font-bold text-white group-hover:text-green-500 transition-colors">Smart Breathe</h4>
                            <span class="text-gray-500 font-mono text-xs">2024</span>
                        </div>
                        <p class="text-gray-400 mb-6 text-sm leading-relaxed">
                            Low-cost adaptive ventilator with telemetry. Adjusts airflow based on real-time patient vitals. 1st Prize Winner at HISET-2024.
                        </p>
                        
                        <div class="border-l-2 border-green-500 pl-4 mb-6">
                            <p class="text-xs font-mono text-gray-500 uppercase mb-1">Key Achievement</p>
                            <p class="text-sm text-white">Validated air discharge of 4.28 Liters/min for COPD support.</p>
                        </div>

                        <div class="flex flex-wrap gap-2">
                            <span class="tech-tag bg-gray-800 text-gray-300">Bio-Feedback</span>
                            <span class="tech-tag bg-gray-800 text-gray-300">Nema-17</span>
                            <span class="tech-tag bg-gray-800 text-gray-300">ThingSpeak</span>
                        </div>
                    </div>
                </div>

            </div>
            
            <!-- More Projects Grid (Compact) -->
            <div class="mt-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="border border-blueprint-700 bg-blueprint-800 p-6 hover:border-neon-cyan transition-colors">
                    <h5 class="font-mono text-neon-cyan text-sm mb-2">005_TRINETRA</h5>
                    <p class="text-white font-bold mb-2">Solar Panel Robot</p>
                    <p class="text-xs text-gray-400">Pivoting wheel drive for complex array navigation.</p>
                </div>
                <div class="border border-blueprint-700 bg-blueprint-800 p-6 hover:border-neon-cyan transition-colors">
                    <h5 class="font-mono text-neon-cyan text-sm mb-2">006_HYDROGAUGE</h5>
                    <p class="text-white font-bold mb-2">Bladder Level Sensor</p>
                    <p class="text-xs text-gray-400">Pneumatic isolation for corrosive environments.</p>
                </div>
                <div class="border border-blueprint-700 bg-blueprint-800 p-6 hover:border-neon-cyan transition-colors">
                    <h5 class="font-mono text-neon-cyan text-sm mb-2">007_AVIBHUJ</h5>
                    <p class="text-white font-bold mb-2">SAE ATV Roll Cage</p>
                    <p class="text-xs text-gray-400">Safety Factor 2.97 with optimized torsion.</p>
                </div>
                <div class="border border-blueprint-700 bg-blueprint-800 p-6 hover:border-neon-cyan transition-colors">
                    <h5 class="font-mono text-neon-cyan text-sm mb-2">008_CLOUD_NODE</h5>
                    <p class="text-white font-bold mb-2">Biometric Sync</p>
                    <p class="text-xs text-gray-400">Direct Google Sheet injection via ESP8266.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="py-24 bg-blueprint-900 border-y border-blueprint-700">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-neon-orange font-mono text-sm uppercase tracking-widest mb-12">02. The Toolkit</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
                <!-- Skill Column 1 -->
                <div class="space-y-6">
                    <div class="w-16 h-16 mx-auto border border-gray-600 rounded-full flex items-center justify-center bg-gray-900 text-neon-orange">
                         <!-- CAD Icon -->
                         <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                         </svg>
                    </div>
                    <h3 class="text-xl font-bold text-white">Design & Analysis</h3>
                    <ul class="space-y-2 font-mono text-sm text-gray-400">
                        <li>SolidWorks (CSWA)</li>
                        <li>CATIA V5</li>
                        <li>ANSYS Workbench</li>
                        <li>KeyShot Rendering</li>
                    </ul>
                </div>

                <!-- Skill Column 2 -->
                <div class="space-y-6">
                    <div class="w-16 h-16 mx-auto border border-gray-600 rounded-full flex items-center justify-center bg-gray-900 text-neon-cyan">
                         <!-- Code Icon -->
                         <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                         </svg>
                    </div>
                    <h3 class="text-xl font-bold text-white">IoT & Embedded</h3>
                    <ul class="space-y-2 font-mono text-sm text-gray-400">
                        <li>C / C++</li>
                        <li>ESP32 / ESP8266</li>
                        <li>Raspberry Pi</li>
                        <li>Google Apps Script</li>
                    </ul>
                </div>

                <!-- Skill Column 3 -->
                <div class="space-y-6">
                    <div class="w-16 h-16 mx-auto border border-gray-600 rounded-full flex items-center justify-center bg-gray-900 text-green-500">
                         <!-- Build Icon -->
                         <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                         </svg>
                    </div>
                    <h3 class="text-xl font-bold text-white">Fabrication</h3>
                    <ul class="space-y-2 font-mono text-sm text-gray-400">
                        <li>3D Printing (FDM)</li>
                        <li>DFM & DFA</li>
                        <li>Rapid Prototyping</li>
                        <li>Mechanism Design</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer / Contact -->
    <footer id="contact" class="bg-black text-gray-400 py-16 border-t border-gray-800">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <h2 class="text-3xl font-bold text-white mb-8">Ready to Engineer the Future?</h2>
            
            <div class="inline-block bg-gray-900 border border-gray-800 p-8 rounded-lg mb-8 text-left w-full md:w-auto">
                <div class="font-mono text-sm space-y-4">
                    <p><span class="text-neon-orange">></span> email: <a href="mailto:nilovemandal@gmail.com" class="text-white hover:text-neon-cyan hover:underline">nilovemandal@gmail.com</a></p>
                    <p><span class="text-neon-orange">></span> phone: <span class="text-white">+91 93074 74959</span></p>
                    <p><span class="text-neon-orange">></span> loc: <span class="text-white">Jalgaon Jamod, India</span></p>
                </div>
            </div>

            <div class="flex justify-center space-x-4 mb-8">
                <a href="#" class="p-3 bg-gray-900 rounded-full hover:bg-neon-cyan hover:text-black transition-all">
                    <!-- GitHub (Simulated) -->
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                    </svg>
                </a>
                <a href="#" class="p-3 bg-gray-900 rounded-full hover:bg-neon-cyan hover:text-black transition-all">
                    <!-- LinkedIn (Simulated) -->
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                    </svg>
                </a>
            </div>

            <p class="text-xs font-mono text-gray-600">
                &copy; 2025 Nilove Mandal. Designed with Kinetic Blueprint v1.0
            </p>
        </div>
    </footer>

    <!-- Scripts -->
    <script>
        // X-Ray Mode Toggle Logic
        const toggle = document.getElementById('xray-toggle');
        const body = document.body;

        toggle.addEventListener('change', () => {
            if (toggle.checked) {
                body.classList.add('wireframe-mode');
            } else {
                body.classList.remove('wireframe-mode');
            }
        });

        // Three.js Logic for Hero Section
        const initThreeJS = () => {
            const container = document.getElementById('canvas-container');
            
            // Scene setup
            const scene = new THREE.Scene();
            // Fog for depth fading
            scene.fog = new THREE.FogExp2(0x0a0a0f, 0.001);

            // Camera
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 20;

            // Renderer
            const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            container.appendChild(renderer.domElement);

            // Object: Large Wireframe Icosahedron
            const geometry = new THREE.IcosahedronGeometry(10, 1);
            const material = new THREE.MeshBasicMaterial({ 
                color: 0x2d3e50, 
                wireframe: true,
                transparent: true,
                opacity: 0.3
            });
            const sphere = new THREE.Mesh(geometry, material);
            scene.add(sphere);

            // Object: Inner Core (representing the "Idea")
            const coreGeo = new THREE.IcosahedronGeometry(4, 0);
            const coreMat = new THREE.MeshBasicMaterial({
                color: 0x00f0ff,
                wireframe: true,
                transparent: true,
                opacity: 0.5
            });
            const core = new THREE.Mesh(coreGeo, coreMat);
            scene.add(core);

            // Particles
            const particlesGeo = new THREE.BufferGeometry();
            const particlesCount = 200;
            const posArray = new Float32Array(particlesCount * 3);

            for(let i = 0; i < particlesCount * 3; i++) {
                posArray[i] = (Math.random() - 0.5) * 60;
            }

            particlesGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
            const particlesMat = new THREE.PointsMaterial({
                size: 0.1,
                color: 0xff5e00,
                transparent: true,
                opacity: 0.8
            });
            const particles = new THREE.Points(particlesGeo, particlesMat);
            scene.add(particles);

            // Animation Loop
            let mouseX = 0;
            let mouseY = 0;
            let targetX = 0;
            let targetY = 0;

            const windowHalfX = window.innerWidth / 2;
            const windowHalfY = window.innerHeight / 2;

            document.addEventListener('mousemove', (event) => {
                mouseX = (event.clientX - windowHalfX);
                mouseY = (event.clientY - windowHalfY);
            });

            const animate = () => {
                requestAnimationFrame(animate);

                targetX = mouseX * 0.001;
                targetY = mouseY * 0.001;

                sphere.rotation.y += 0.002;
                sphere.rotation.x += 0.001;
                
                core.rotation.y -= 0.005;
                core.rotation.x -= 0.005;

                // Subtle mouse interactivity
                sphere.rotation.y += 0.05 * (targetX - sphere.rotation.y);
                sphere.rotation.x += 0.05 * (targetY - sphere.rotation.x);

                particles.rotation.y = -mouseX * 0.0002;
                particles.rotation.x = -mouseY * 0.0002;

                renderer.render(scene, camera);
            };

            animate();

            // Resize Handler
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        };

        // Initialize only if WebGL is available
        try {
            initThreeJS();
        } catch (e) {
            console.log("WebGL not supported, falling back to CSS background");
        }
    </script>
</body>
</html>
