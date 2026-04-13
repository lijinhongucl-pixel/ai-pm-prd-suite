/**
 * 主交互逻辑
 * 所有渲染基于 data.js 中的数据动态计算
 */

// 渲染功能卡片
function renderFeatures() {
    const grid = document.getElementById('featureGrid');
    if (!grid || typeof FEATURES === 'undefined') return;
    
    // 动态计算功能数量
    const featureCount = Object.keys(FEATURES).length;
    console.log(`渲染 ${featureCount} 个功能卡片`);
    
    grid.innerHTML = Object.entries(FEATURES).map(([key, feature]) => `
        <div class="feature-card">
            <div class="feature-card-icon">${feature.icon || '⭐'}</div>
            <h3 class="feature-card-title">${feature.title}</h3>
            <p class="feature-card-desc">${feature.description}</p>
        </div>
    `).join('');
}

// 渲染统计数据
function renderStats() {
    const grid = document.getElementById('statsGrid');
    if (!grid || typeof STATS === 'undefined') return;
    
    // 动态计算统计数量
    const statsCount = Object.keys(STATS).length;
    console.log(`渲染 ${statsCount} 个统计卡片`);
    
    grid.innerHTML = Object.entries(STATS).map(([key, stat]) => `
        <div class="stat-card">
            <div class="stat-value">${stat.value}${stat.suffix || ''}</div>
            <div class="stat-label">${stat.label}</div>
        </div>
    `).join('');
}

// 平滑滚动
function smoothScroll(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

// 导航点击事件
function initNavigation() {
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const target = item.getAttribute('href');
            if (target && target !== '#') {
                smoothScroll(target);
            }
            
            // 更新激活状态
            document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
            item.classList.add('active');
        });
    });
}

// 按钮点击动画
function initButtons() {
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            // 创建涟漪效果
            const ripple = document.createElement('span');
            ripple.style.cssText = `
                position: absolute;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s ease-out;
                pointer-events: none;
            `;
            
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
            ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
        });
    });
    
    // 添加涟漪动画
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
}

// 滚动时更新导航状态
function initScrollSpy() {
    const sections = document.querySelectorAll('section');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id || entry.target.className.split(' ')[0];
                document.querySelectorAll('.nav-item').forEach(item => {
                    item.classList.toggle('active', item.getAttribute('href') === `#${id}`);
                });
            }
        });
    }, { threshold: 0.5 });
    
    sections.forEach(section => observer.observe(section));
}

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    renderFeatures();
    renderStats();
    initNavigation();
    initButtons();
    initScrollSpy();
    
    console.log('原型初始化完成');
});
