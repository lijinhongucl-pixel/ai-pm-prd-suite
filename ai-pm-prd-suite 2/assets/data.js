/**
 * 数据配置文件
 * 所有数据在此集中管理，UI 通过动态计算渲染
 */

// 功能列表数据
const FEATURES = {
    feature1: {
        title: "智能分析",
        description: "AI 驱动的智能分析能力，快速洞察数据价值",
        icon: "📊"
    },
    feature2: {
        title: "实时协作",
        description: "多人实时协作，提升团队效率",
        icon: "👥"
    },
    feature3: {
        title: "安全可靠",
        description: "企业级安全防护，数据安全保障",
        icon: "🔒"
    },
    feature4: {
        title: "易于集成",
        description: "丰富的 API 接口，快速集成现有系统",
        icon: "🔌"
    }
};

// 统计数据
const STATS = {
    users: {
        value: 10000,
        label: "活跃用户",
        suffix: "+"
    },
    projects: {
        value: 5000,
        label: "项目数量",
        suffix: "+"
    },
    satisfaction: {
        value: 98,
        label: "用户满意度",
        suffix: "%"
    },
    uptime: {
        value: 99.9,
        label: "服务可用性",
        suffix: "%"
    }
};

// 导出数据（供 main.js 使用）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { FEATURES, STATS };
}
