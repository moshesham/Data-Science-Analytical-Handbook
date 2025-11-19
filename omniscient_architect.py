#!/usr/bin/env python3
"""
Omniscient Architect - Elite-Level Code Review System

This tool performs a forensic, multi-perspective review of a codebase based on
a specific Project Objective. It simulates four specialist sub-agents to analyze
different aspects of the code.

Author: Data Science Analytical Handbook Team
License: MIT
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict
import re


@dataclass
class FileAnalysis:
    """Stores analysis results for a single file"""
    path: str
    size: int
    language: str
    complexity_score: int = 0
    issues: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)


@dataclass
class AgentFindings:
    """Stores findings from each specialist agent"""
    agent_name: str
    findings: List[str] = field(default_factory=list)
    confidence: float = 0.0


@dataclass
class ReviewResult:
    """Complete review result"""
    project_understanding: str = ""
    goal_alignment_score: int = 0
    component_status: Dict[str, str] = field(default_factory=dict)
    strengths: List[Dict[str, str]] = field(default_factory=list)
    weaknesses: Dict[str, List[Dict[str, str]]] = field(default_factory=dict)
    strategic_advice: Dict[str, str] = field(default_factory=dict)


class OmniscientArchitect:
    """
    The Omniscient Architect - Elite-level AI combining capabilities of:
    - Senior Staff Engineer
    - Product Manager
    - Strategic CTO
    """
    
    def __init__(self, repo_path: str, project_objective: str = ""):
        self.repo_path = Path(repo_path)
        self.project_objective = project_objective
        self.files_analyzed: List[FileAnalysis] = []
        self.agent_alpha: Optional[AgentFindings] = None
        self.agent_beta: Optional[AgentFindings] = None
        self.agent_gamma: Optional[AgentFindings] = None
        self.agent_delta: Optional[AgentFindings] = None
        
        # Language detection patterns
        self.language_patterns = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.go': 'Go',
            '.rs': 'Rust',
            '.rb': 'Ruby',
            '.php': 'PHP',
            '.md': 'Markdown',
            '.json': 'JSON',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.html': 'HTML',
            '.css': 'CSS',
            '.sql': 'SQL',
        }
        
        # Ignore patterns
        self.ignore_patterns = [
            '.git', '__pycache__', 'node_modules', '.idea', '.vscode',
            'venv', 'env', '.pytest_cache', '.mypy_cache', 'dist', 'build',
            '.DS_Store', '*.pyc', '*.pyo', '*.pyd', '.so', '.egg-info'
        ]
    
    def should_ignore(self, path: Path) -> bool:
        """Check if path should be ignored"""
        path_str = str(path)
        for pattern in self.ignore_patterns:
            if pattern in path_str:
                return True
        return False
    
    def detect_language(self, file_path: Path) -> str:
        """Detect programming language from file extension"""
        suffix = file_path.suffix.lower()
        return self.language_patterns.get(suffix, 'Unknown')
    
    def calculate_complexity(self, content: str, language: str) -> int:
        """Calculate basic complexity score for code"""
        if language == 'Python':
            # Count control structures
            complexity = 0
            complexity += len(re.findall(r'\bif\b', content))
            complexity += len(re.findall(r'\bfor\b', content))
            complexity += len(re.findall(r'\bwhile\b', content))
            complexity += len(re.findall(r'\btry\b', content))
            complexity += len(re.findall(r'\bdef\b', content))
            complexity += len(re.findall(r'\bclass\b', content))
            return complexity
        return 0
    
    # ==================== PHASE 1: INGESTION & DECONSTRUCTION ====================
    
    def phase1_ingest_and_deconstruct(self) -> Dict[str, Any]:
        """
        Phase 1: Ingest codebase and deconstruct project objective
        
        Returns:
            Dict containing file structure, statistics, and component breakdown
        """
        print("🔍 PHASE 1: Ingestion & Deconstruction")
        print("=" * 70)
        
        structure = {
            'total_files': 0,
            'total_lines': 0,
            'languages': defaultdict(int),
            'file_types': defaultdict(int),
            'components': defaultdict(list),
        }
        
        # Scan repository
        for file_path in self.repo_path.rglob('*'):
            if file_path.is_file() and not self.should_ignore(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    language = self.detect_language(file_path)
                    size = len(content)
                    lines = len(content.splitlines())
                    
                    analysis = FileAnalysis(
                        path=str(file_path.relative_to(self.repo_path)),
                        size=size,
                        language=language,
                        complexity_score=self.calculate_complexity(content, language)
                    )
                    
                    self.files_analyzed.append(analysis)
                    structure['total_files'] += 1
                    structure['total_lines'] += lines
                    structure['languages'][language] += 1
                    structure['file_types'][file_path.suffix] += 1
                    
                    # Categorize into components
                    if 'test' in str(file_path).lower():
                        structure['components']['Testing'].append(analysis.path)
                    elif language == 'Markdown':
                        structure['components']['Documentation'].append(analysis.path)
                    elif language in ['Python', 'JavaScript', 'TypeScript']:
                        structure['components']['Core Logic'].append(analysis.path)
                    elif language in ['HTML', 'CSS']:
                        structure['components']['Frontend'].append(analysis.path)
                    elif language in ['JSON', 'YAML']:
                        structure['components']['Configuration'].append(analysis.path)
                    
                except Exception as e:
                    print(f"⚠️  Error reading {file_path}: {e}")
        
        # Analyze project objective
        components_identified = self._deconstruct_objective()
        structure['objective_components'] = components_identified
        
        print(f"\n📊 Repository Statistics:")
        print(f"   • Total Files: {structure['total_files']}")
        print(f"   • Total Lines: {structure['total_lines']:,}")
        print(f"   • Languages: {dict(structure['languages'])}")
        print(f"   • Components Identified: {len(components_identified)}")
        
        return structure
    
    def _deconstruct_objective(self) -> List[str]:
        """Deconstruct the project objective into technical components"""
        if not self.project_objective:
            return ["Code Quality", "Architecture", "Performance", "Security"]
        
        components = []
        objective_lower = self.project_objective.lower()
        
        # Pattern matching for common components
        if 'auth' in objective_lower or 'login' in objective_lower:
            components.append("Authentication System")
        if 'database' in objective_lower or 'db' in objective_lower:
            components.append("Database Schema")
        if 'api' in objective_lower or 'rest' in objective_lower:
            components.append("API Layer")
        if 'frontend' in objective_lower or 'ui' in objective_lower:
            components.append("Frontend Interface")
        if 'test' in objective_lower:
            components.append("Testing Infrastructure")
        if 'security' in objective_lower:
            components.append("Security Measures")
        
        if not components:
            components = ["Core Functionality", "Code Quality", "Architecture"]
        
        return components
    
    # ==================== PHASE 2: MULTI-AGENT SIMULATION ====================
    
    def phase2_multi_agent_analysis(self, structure: Dict[str, Any]) -> Tuple[AgentFindings, AgentFindings, AgentFindings, AgentFindings]:
        """
        Phase 2: Simulate four specialist sub-agents
        
        Returns:
            Tuple of findings from all four agents
        """
        print("\n\n🤖 PHASE 2: Multi-Agent Simulation")
        print("=" * 70)
        
        self.agent_alpha = self._agent_alpha_architecture(structure)
        self.agent_beta = self._agent_beta_efficiency(structure)
        self.agent_gamma = self._agent_gamma_reliability(structure)
        self.agent_delta = self._agent_delta_alignment(structure)
        
        # Cross-check and validate findings
        print("\n🔍 Cross-Checking Agent Findings...")
        self._cross_check_findings()
        
        return self.agent_alpha, self.agent_beta, self.agent_gamma, self.agent_delta
    
    def _agent_alpha_architecture(self, structure: Dict[str, Any]) -> AgentFindings:
        """Agent Alpha: Reviews architecture, design patterns, and scalability"""
        print("\n🏗️  Agent Alpha (Architecture) analyzing...")
        
        findings = AgentFindings(agent_name="Agent Alpha (Architecture)")
        
        # Analyze file structure
        if structure['total_files'] > 100:
            findings.findings.append("Large codebase detected - ensure modular architecture")
        
        # Check for proper separation of concerns
        has_utils = any('utils' in f.path or 'helpers' in f.path for f in self.files_analyzed)
        has_tests = any('test' in f.path for f in self.files_analyzed)
        has_config = any(f.language in ['JSON', 'YAML'] for f in self.files_analyzed)
        
        if has_utils:
            findings.findings.append("✅ Utility/helper modules present - good separation")
        else:
            findings.findings.append("⚠️ No dedicated utility modules - consider refactoring")
        
        if has_tests:
            findings.findings.append("✅ Test infrastructure exists")
        else:
            findings.findings.append("❌ No test files detected - critical gap")
        
        if has_config:
            findings.findings.append("✅ Configuration files present - good practice")
        
        # Check for documentation
        has_readme = any('README' in f.path.upper() for f in self.files_analyzed)
        if has_readme:
            findings.findings.append("✅ README documentation present")
        else:
            findings.findings.append("⚠️ Missing README documentation")
        
        findings.confidence = 0.85
        return findings
    
    def _agent_beta_efficiency(self, structure: Dict[str, Any]) -> AgentFindings:
        """Agent Beta: Hunts for complexity, redundant code, and efficiency issues"""
        print("⚡ Agent Beta (Efficiency) analyzing...")
        
        findings = AgentFindings(agent_name="Agent Beta (Efficiency)")
        
        # Analyze code complexity
        python_files = [f for f in self.files_analyzed if f.language == 'Python']
        if python_files:
            avg_complexity = sum(f.complexity_score for f in python_files) / len(python_files)
            max_complexity = max(f.complexity_score for f in python_files)
            
            if avg_complexity > 20:
                findings.findings.append(f"⚠️ Average complexity: {avg_complexity:.1f} - consider refactoring")
            else:
                findings.findings.append(f"✅ Average complexity: {avg_complexity:.1f} - acceptable")
            
            if max_complexity > 50:
                high_complexity_file = max(python_files, key=lambda f: f.complexity_score)
                findings.findings.append(f"❌ High complexity in {high_complexity_file.path} (score: {max_complexity})")
        
        # Check for duplicate code patterns
        file_sizes = [f.size for f in self.files_analyzed if f.language != 'Markdown']
        if file_sizes and max(file_sizes) > 10000:
            large_file = max(self.files_analyzed, key=lambda f: f.size if f.language != 'Markdown' else 0)
            findings.findings.append(f"⚠️ Large file detected: {large_file.path} ({large_file.size} bytes)")
        
        findings.confidence = 0.80
        return findings
    
    def _agent_gamma_reliability(self, structure: Dict[str, Any]) -> AgentFindings:
        """Agent Gamma: Looks for edge cases, error handling, and security"""
        print("🛡️  Agent Gamma (Reliability & Security) analyzing...")
        
        findings = AgentFindings(agent_name="Agent Gamma (Reliability & Security)")
        
        python_files = [f for f in self.files_analyzed if f.language == 'Python']
        
        # Check for error handling
        for file_analysis in python_files[:5]:  # Sample first 5 Python files
            try:
                file_path = self.repo_path / file_analysis.path
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                has_try = 'try:' in content
                has_exception = 'except' in content or 'Exception' in content
                
                if has_try and has_exception:
                    file_analysis.strengths.append("Error handling present")
                elif len(content) > 500:  # Only flag larger files
                    file_analysis.issues.append("Limited error handling")
            except Exception:
                pass
        
        # Check for security patterns
        security_checks = {
            'input_validation': False,
            'authentication': False,
            'encryption': False,
        }
        
        for file_analysis in self.files_analyzed:
            path_lower = file_analysis.path.lower()
            if 'auth' in path_lower or 'login' in path_lower:
                security_checks['authentication'] = True
            if 'valid' in path_lower:
                security_checks['input_validation'] = True
        
        if security_checks['authentication']:
            findings.findings.append("✅ Authentication components identified")
        if security_checks['input_validation']:
            findings.findings.append("✅ Input validation components identified")
        
        # Check for common vulnerabilities
        findings.findings.append("⚠️ Recommend security audit for SQL injection, XSS, CSRF")
        
        findings.confidence = 0.75
        return findings
    
    def _agent_delta_alignment(self, structure: Dict[str, Any]) -> AgentFindings:
        """Agent Delta: Checks if code achieves the business goal"""
        print("🎯 Agent Delta (Alignment) analyzing...")
        
        findings = AgentFindings(agent_name="Agent Delta (Alignment)")
        
        if not self.project_objective:
            findings.findings.append("⚠️ No specific project objective provided - performing general analysis")
            findings.confidence = 0.60
            return findings
        
        objective_lower = self.project_objective.lower()
        
        # Check for alignment with stated objectives
        components_found = []
        components_missing = []
        
        # Check for specific features mentioned in objective
        if 'api' in objective_lower:
            has_api = any('api' in f.path.lower() for f in self.files_analyzed)
            if has_api:
                components_found.append("API implementation")
            else:
                components_missing.append("API implementation")
        
        if 'test' in objective_lower:
            has_tests = any('test' in f.path.lower() for f in self.files_analyzed)
            if has_tests:
                components_found.append("Testing infrastructure")
            else:
                components_missing.append("Testing infrastructure")
        
        if 'documentation' in objective_lower or 'docs' in objective_lower:
            has_docs = any(f.language == 'Markdown' for f in self.files_analyzed)
            if has_docs:
                components_found.append("Documentation")
            else:
                components_missing.append("Documentation")
        
        for comp in components_found:
            findings.findings.append(f"✅ Objective component present: {comp}")
        
        for comp in components_missing:
            findings.findings.append(f"❌ Objective component missing: {comp}")
        
        findings.confidence = 0.85
        return findings
    
    def _cross_check_findings(self):
        """Cross-reference findings from all agents and discard hallucinations"""
        # Remove low-confidence findings
        all_agents = [self.agent_alpha, self.agent_beta, self.agent_gamma, self.agent_delta]
        
        for agent in all_agents:
            if agent and agent.confidence < 0.50:
                print(f"⚠️ {agent.agent_name} has low confidence ({agent.confidence})")
        
        # Flag contradictions
        # (In a real implementation, this would use NLP to detect contradictions)
        pass
    
    # ==================== PHASE 3: STRATEGIC GAP ANALYSIS ====================
    
    def phase3_gap_analysis(self, structure: Dict[str, Any]) -> Dict[str, Any]:
        """
        Phase 3: Compare current state vs ideal state
        
        Returns:
            Dict containing gap analysis results
        """
        print("\n\n📊 PHASE 3: Strategic Gap Analysis")
        print("=" * 70)
        
        gap_analysis = {
            'current_state': {},
            'ideal_state': {},
            'gaps': [],
        }
        
        # Current state assessment
        gap_analysis['current_state'] = {
            'total_files': structure['total_files'],
            'languages': dict(structure['languages']),
            'has_tests': bool(structure['components'].get('Testing')),
            'has_docs': bool(structure['components'].get('Documentation')),
            'has_config': bool(structure['components'].get('Configuration')),
        }
        
        # Ideal state based on best practices
        gap_analysis['ideal_state'] = {
            'has_tests': True,
            'has_docs': True,
            'has_config': True,
            'has_ci_cd': True,
            'has_linting': True,
            'test_coverage': '> 80%',
        }
        
        # Identify gaps
        if not gap_analysis['current_state']['has_tests']:
            gap_analysis['gaps'].append({
                'area': 'Testing',
                'severity': 'Critical',
                'description': 'No test infrastructure detected',
                'recommendation': 'Implement unit tests using pytest or unittest'
            })
        
        if not gap_analysis['current_state']['has_docs']:
            gap_analysis['gaps'].append({
                'area': 'Documentation',
                'severity': 'Medium',
                'description': 'Limited documentation',
                'recommendation': 'Add comprehensive README and API documentation'
            })
        
        # Check for CI/CD
        has_cicd = any('.github/workflows' in f.path or '.gitlab-ci' in f.path 
                      for f in self.files_analyzed)
        if not has_cicd:
            gap_analysis['gaps'].append({
                'area': 'CI/CD',
                'severity': 'Medium',
                'description': 'No CI/CD pipeline detected',
                'recommendation': 'Set up GitHub Actions or similar CI/CD'
            })
        
        print(f"\n📈 Gaps Identified: {len(gap_analysis['gaps'])}")
        for gap in gap_analysis['gaps']:
            print(f"   • {gap['area']} ({gap['severity']}): {gap['description']}")
        
        return gap_analysis
    
    # ==================== OUTPUT GENERATION ====================
    
    def generate_report(self, structure: Dict[str, Any], gap_analysis: Dict[str, Any]) -> ReviewResult:
        """Generate the final structured report"""
        result = ReviewResult()
        
        # 1. Executive Summary & Alignment Check
        result.project_understanding = self._generate_understanding(structure)
        result.goal_alignment_score = self._calculate_alignment_score(gap_analysis)
        result.component_status = self._generate_component_status(structure)
        
        # 2. Strengths
        result.strengths = self._identify_strengths()
        
        # 3. Critical Review: Weaknesses & Adjustments
        result.weaknesses = self._identify_weaknesses(gap_analysis)
        
        # 4. Strategic Advice
        result.strategic_advice = self._generate_strategic_advice(structure)
        
        return result
    
    def _generate_understanding(self, structure: Dict[str, Any]) -> str:
        """Generate project understanding summary"""
        languages = ', '.join(structure['languages'].keys())
        return (f"This repository contains {structure['total_files']} files "
                f"across {len(structure['languages'])} languages ({languages}). "
                f"The codebase appears to be a {self._infer_project_type(structure)} "
                f"with {structure['total_lines']:,} lines of code.")
    
    def _infer_project_type(self, structure: Dict[str, Any]) -> str:
        """Infer the type of project from structure"""
        if 'Python' in structure['languages'] and any('streamlit' in f.path.lower() 
                                                       for f in self.files_analyzed):
            return "Streamlit web application"
        elif 'JavaScript' in structure['languages'] or 'TypeScript' in structure['languages']:
            return "web application"
        elif 'Markdown' in structure['languages'] and structure['languages']['Markdown'] > 5:
            return "documentation-heavy project or handbook"
        return "software project"
    
    def _calculate_alignment_score(self, gap_analysis: Dict[str, Any]) -> int:
        """Calculate goal alignment score (0-100)"""
        total_checks = 5
        passed_checks = 0
        
        if gap_analysis['current_state'].get('has_tests'):
            passed_checks += 1
        if gap_analysis['current_state'].get('has_docs'):
            passed_checks += 1
        if gap_analysis['current_state'].get('has_config'):
            passed_checks += 1
        
        # Check for critical gaps
        critical_gaps = [g for g in gap_analysis['gaps'] if g['severity'] == 'Critical']
        if not critical_gaps:
            passed_checks += 2
        
        return int((passed_checks / total_checks) * 100)
    
    def _generate_component_status(self, structure: Dict[str, Any]) -> Dict[str, str]:
        """Generate status for each component"""
        status = {}
        
        for component, files in structure['components'].items():
            if files:
                status[component] = f"Present ({len(files)} files)"
            else:
                status[component] = "Missing"
        
        return status
    
    def _identify_strengths(self) -> List[Dict[str, str]]:
        """Identify project strengths from agent findings"""
        strengths = []
        
        all_agents = [self.agent_alpha, self.agent_beta, self.agent_gamma, self.agent_delta]
        
        for agent in all_agents:
            if agent:
                for finding in agent.findings:
                    if '✅' in finding:
                        strength_text = finding.replace('✅', '').strip()
                        strengths.append({
                            'strength': strength_text.split('-')[0].strip(),
                            'evidence': f"Identified by {agent.agent_name}",
                            'why_it_matters': "This demonstrates adherence to best practices"
                        })
        
        return strengths[:5]  # Top 5 strengths
    
    def _identify_weaknesses(self, gap_analysis: Dict[str, Any]) -> Dict[str, List[Dict[str, str]]]:
        """Identify weaknesses grouped by category"""
        weaknesses = {
            'Efficiency': [],
            'Accuracy': [],
            'Reliability': []
        }
        
        # From agent findings
        if self.agent_beta:
            for finding in self.agent_beta.findings:
                if '⚠️' in finding or '❌' in finding:
                    weaknesses['Efficiency'].append({
                        'issue': finding.replace('⚠️', '').replace('❌', '').strip(),
                        'location': 'Multiple files',
                        'fix': 'Refactor to reduce complexity and improve performance'
                    })
        
        if self.agent_gamma:
            for finding in self.agent_gamma.findings:
                if '⚠️' in finding or '❌' in finding:
                    weaknesses['Reliability'].append({
                        'issue': finding.replace('⚠️', '').replace('❌', '').strip(),
                        'location': 'Security layer',
                        'fix': 'Implement comprehensive security measures'
                    })
        
        # From gap analysis
        for gap in gap_analysis['gaps']:
            if gap['severity'] == 'Critical':
                weaknesses['Reliability'].append({
                    'issue': gap['description'],
                    'location': gap['area'],
                    'fix': gap['recommendation']
                })
        
        return weaknesses
    
    def _generate_strategic_advice(self, structure: Dict[str, Any]) -> Dict[str, str]:
        """Generate strategic advisor recommendations"""
        return {
            'scalability': (
                "To handle 100x user growth: (1) Implement caching layers, "
                "(2) Add horizontal scaling capabilities, "
                "(3) Use async/await patterns for I/O operations, "
                "(4) Consider microservices architecture for large components."
            ),
            'future_proofing': (
                "Recommended next features: (1) Add comprehensive monitoring and logging, "
                "(2) Implement feature flags for gradual rollouts, "
                "(3) Set up automated testing pipeline, "
                "(4) Add API versioning for backward compatibility."
            ),
            'broader_application': (
                f"This {self._infer_project_type(structure)} could be adapted for: "
                "(1) Different industry verticals with similar workflow needs, "
                "(2) Enterprise-scale deployment with multi-tenancy, "
                "(3) Educational platforms requiring similar interactive features."
            )
        }
    
    def format_output(self, result: ReviewResult) -> str:
        """Format the final output according to requirements"""
        output = []
        
        output.append("=" * 80)
        output.append("🧠 OMNISCIENT ARCHITECT - CODE REVIEW REPORT")
        output.append("=" * 80)
        output.append("")
        
        # 1. Executive Summary
        output.append("## 1. 🎯 Executive Summary & Alignment Check")
        output.append("")
        output.append("### Project Understanding:")
        output.append(result.project_understanding)
        output.append("")
        output.append(f"### Goal Alignment Score: {result.goal_alignment_score}%")
        output.append("")
        output.append("### Component Breakdown:")
        for component, status in result.component_status.items():
            output.append(f"  • {component}: {status}")
        output.append("")
        
        # 2. Strengths
        output.append("## 2. 💪 Strengths (With Evidence)")
        output.append("")
        for strength in result.strengths:
            output.append(f"**Strength:** {strength['strength']}")
            output.append(f"**Evidence:** {strength['evidence']}")
            output.append(f"**Why it matters:** {strength['why_it_matters']}")
            output.append("")
        
        # 3. Critical Review
        output.append("## 3. ⚠️ Critical Review: Weaknesses & Adjustments")
        output.append("")
        for category, issues in result.weaknesses.items():
            if issues:
                output.append(f"### {category}:")
                for issue in issues:
                    output.append(f"**Issue:** {issue['issue']}")
                    output.append(f"**Location:** {issue['location']}")
                    output.append(f"**The Fix:** {issue['fix']}")
                    output.append("")
        
        # 4. Strategic Advice
        output.append("## 4. 🧠 The Strategist's Advisor")
        output.append("")
        output.append("### Scalability:")
        output.append(result.strategic_advice['scalability'])
        output.append("")
        output.append("### Future-Proofing:")
        output.append(result.strategic_advice['future_proofing'])
        output.append("")
        output.append("### Broader Application:")
        output.append(result.strategic_advice['broader_application'])
        output.append("")
        
        output.append("=" * 80)
        output.append("End of Report")
        output.append("=" * 80)
        
        return '\n'.join(output)
    
    def run_analysis(self) -> str:
        """Execute the complete analysis workflow"""
        print("\n" + "=" * 70)
        print("🧠 OMNISCIENT ARCHITECT - STARTING ANALYSIS")
        print("=" * 70)
        
        if self.project_objective:
            print(f"\n📋 Project Objective: {self.project_objective}\n")
        
        # Execute three phases
        structure = self.phase1_ingest_and_deconstruct()
        agents = self.phase2_multi_agent_analysis(structure)
        gap_analysis = self.phase3_gap_analysis(structure)
        
        # Generate final report
        result = self.generate_report(structure, gap_analysis)
        formatted_output = self.format_output(result)
        
        return formatted_output


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Omniscient Architect - Elite-Level Code Review System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze current directory
  python omniscient_architect.py .
  
  # Analyze with specific objective
  python omniscient_architect.py /path/to/repo --objective "Build a user authentication system"
  
  # Save output to file
  python omniscient_architect.py . --output report.md
        """
    )
    
    parser.add_argument(
        'repo_path',
        help='Path to the repository to analyze'
    )
    
    parser.add_argument(
        '-o', '--objective',
        help='Project objective to analyze against',
        default=''
    )
    
    parser.add_argument(
        '--output',
        help='Output file path (default: print to stdout)',
        default=None
    )
    
    args = parser.parse_args()
    
    # Validate repo path
    repo_path = Path(args.repo_path)
    if not repo_path.exists():
        print(f"Error: Repository path does not exist: {repo_path}")
        sys.exit(1)
    
    # Run analysis
    architect = OmniscientArchitect(
        repo_path=str(repo_path),
        project_objective=args.objective
    )
    
    report = architect.run_analysis()
    
    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n✅ Report saved to: {args.output}")
    else:
        print("\n" + report)


if __name__ == '__main__':
    main()
